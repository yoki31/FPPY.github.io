from django.db.models.aggregates import Count
from django.http import response
from django.test import TestCase, Client
from django.urls import reverse

from doctors.views import appointment, package
from .models import *
from .forms import *
from django.contrib.auth.models import User, Group
from django.contrib.auth.hashers import make_password
import datetime
# Create your tests here.
class TestViewsCase(TestCase):
    
    def setUp(self):
        """"setUp Models.py"""

        password = make_password('user123456')
        user = User.objects.create(username="user", password=password)
        patient = Patient.objects.create(user=user, First_name="Fname", Last_name="Lname", email= "user@example.com", phone="0987654321")
        doctorT = Doctor.objects.create(First_name="DFname", Last_name="DLname", email="doc@example.com", phone="0999999999")
        article = Article.objects.create(doctor=doctorT, header="Test", context="Lorem")
        news = New.objects.create(header="TestNews", context="Lorem20")
        package = Package.objects.create(name="Package_name", price=3000, desc="detail", cond="condition")
        appointment = Appointment.objects.create(Patient_id=patient, Doctor_id=doctorT, symptom="symptom", dateapp=datetime.date(1997, 10, 19))#ไม่ชัวร์
        buy = Buy.objects.create(patient=patient, package=package)
        
        self.group = Group(name="Patient")
        self.group.save()
        self.group = Group(name="Admin")
        self.group.save()

        self.user_ad = User.objects.create_user(username="ad", email="ad@test.com", password="testad")
        self.user = User.objects.create_user(username="test", email="test@test.com", password="test")
        group_ad = Group.objects.get(name="Admin")
        self.user_ad.groups.add(group_ad)

        group_p = Group.objects.get(name="Patient")
        self.user.groups.add(group_p)
        self.patient = Patient.objects.create(user=self.user, First_name="PFname", Last_name="PLname", email= "test@test.com", phone="0123456789")


    def test_index(self):
        self.c = Client()
        response = self.c.get(reverse('doctors:index'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'doctors/index.html', 'doctors/layout.html')
        
    def test_maps(self):
        self.c = Client()
        response = self.c.get(reverse('doctors:maps'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'doctors/maps.html', 'doctors/layout.html')
        
    def test_news(self):
        self.c = Client()
        response = self.c.get(reverse('doctors:news'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'doctors/news.html', 'doctors/layout.html')
        
    def test_about(self):
        self.c = Client()
        response = self.c.get(reverse('doctors:about'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'doctors/about.html', 'doctors/layout.html')
        
        
    def test_requirement(self):
        self.c = Client()
        response = self.c.get(reverse('doctors:project_requirement'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'doctors/requirement.html', 'doctors/layout.html')
    
    
    def test_healthblog(self):
        self.c = Client()
        response = self.c.get(reverse('doctors:healthblog'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'doctors/healthblog.html', 'doctors/layout.html')
    
    
    def test_healthblog_one(self):
        self.c = Client()
        article1 = Article.objects.first()
        response = self.c.get(reverse('doctors:healthblog_content', args=(str(article1.id),)), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'doctors/healthblog_one.html', 'doctors/layout.html')
        
    def test_addArticle_invalid(self):
        self.c = Client()
        self.c.login(username='test', password='test')
        
        self.assertEqual(Article.objects.all().count(), 1)
        doctor1 = Doctor.objects.first()
        response = self.c.post(reverse('doctors:addArticle'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'doctors/addhealthblog.html', 'doctors/layout.html')


    """
    # Not work
    def test_addArticle_valid(self):
        self.c = Client()
        self.c.login(username='test', password='test')
        doctor1 = Doctor.objects.first()
        self.assertEqual(Article.objects.all().count(), 1)
        
        form_data = {'header': 'TestArticle', 'doctor':doctor1, 'context': 'Lorem10', 'img': "defaultpic.jpeg"}
        form = CreateArticleForm(form_data)
        self.assertTrue(form)

        # newarticle = Article.objects.create(doctor=doctor1, header="TestArticle", context="Lorem10")
        
        response = self.c.post(reverse('doctors:addArticle', args=(form_data)), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'doctors/healthblog_one.html', 'doctors/layout.html')
    """
    
    def test_updateArticle_invalid(self):
        self.c = Client()
        article1 = Article.objects.first()
        # form_data = {'header': 'TestArticle', 'doctor':doctor1, 'context': 'Lorem10', 'img': "defaultpic.jpeg"}
        form = CreateArticleForm(instance=article1)
        self.assertTrue(form)
        
        response = self.c.post(reverse('doctors:updateArticle', args=(str(article1.id),)), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'doctors/updatehealthblog.html', 'doctors/layout.html')

    def test_profile(self):
        self.c = Client()
        self.c.login(username='test', password='test')
        response = self.c.get(reverse('doctors:profile'), follow=True)
        self.assertEqual(response.status_code, 200)

    def test_deleteArticle(self):
        self.c = Client()
        article1 = Article.objects.first()
        response = self.c.post(reverse('doctors:deleteArticle', args=(str(article1.id),)), follow=True)
        
        self.assertTemplateUsed(response, 'doctors/healthblog.html', 'doctors/layout.html')
        
    def test_newscontent(self):
        self.c = Client()
        news1 = New.objects.first()
        response = self.c.get(reverse('doctors:news_content', args=(str(news1.id),)), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'doctors/news_one.html', 'doctors/layout.html')

<<<<<<< Updated upstream
    # def test_deletenews(self):
    #     self.c = Client()
    #     news1 = New.objects.first()
    #     response = self.c.post(reverse('doctors:deleteNews', args=(str(news1.id),)), follow=True)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'doctors/news.html', 'doctors/layout.html')
 
    def test_addNews_invalid(self):
        self.c = Client()
        self.c.login(username='test', password='test')
            
        self.assertEqual(New.objects.all().count(), 1)
        # doctor1 = Doctor.objects.first()
        response = self.c.post(reverse('doctors:addNews'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'doctors/addnews.html', 'doctors/layout.html')
  
    def test_updateNew_invalid(self):
        self.c = Client()
        new1 = New.objects.first()
        # form_data = {'header': 'TestArticle', 'doctor':doctor1, 'context': 'Lorem10', 'img': "defaultpic.jpeg"}
        form = CreateNewsForm(instance=new1)
        self.assertTrue(form)
        
        response = self.c.post(reverse('doctors:updateNew', args=(str(new1.id),)), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'doctors/updatenews.html', 'doctors/layout.html')

=======
    def test_deletenews(self):
        self.c = Client()
        news1 = New.objects.first()
        response = self.c.post(reverse('doctors:deleteNews', args=(str(news1.id),)), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'doctors/news.html', 'doctors/layout.html')
    
>>>>>>> Stashed changes
    def test_package(self):
        self.c = Client()
        response = self.c.get(reverse('doctors:package'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'doctors/package.html', 'doctors/layout.html')

    def test_packagecontent(self):
        self.c = Client()
        package1 = Package.objects.first()
        response = self.c.get(reverse('doctors:package_content', args=(str(package1.id),)), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'doctors/package_one.html', 'doctors/layout.html')
    
    def test_editpackage_invalid(self):
        self.c = Client()
        package1 = Package.objects.first()
        form = CreatePackageForm(instance=package1)
        self.assertTrue(form)
        response = self.c.post(reverse('doctors:editpackage', args=(str(package1.id),)), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'doctors/editpackage.html', 'doctors/layout.html')

    def test_deletePackage(self):
        self.c = Client()
        package1 = Package.objects.first()
        response = self.c.post(reverse('doctors:deletepackage', args=(str(package1.id),)), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'doctors/package.html', 'doctors/layout.html')

    def test_addPackage_invalid(self):  ##
        self.c = Client()
        self.c.login(username='test', password='test')
        response = self.c.post(reverse('doctors:addPackage'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'doctors/addpackage.html', 'doctors/layout.html')
        self.assertEqual(Package.objects.all().count(), 1)
    
<<<<<<< Updated upstream
    def test_buy(self): 
        self.c = Client()
        self.c.login(username='test', password='test')
        package1 = Package.objects.first()
        response = self.c.post(reverse('doctors:buy', args=(str(package1.id),)), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'doctors/package.html', 'doctors/layout.html')
        # patient_id = Patient.objects.filter(user=self.c).id
        # self.assertEqual(Buy.objects.filter(patient=patient_id).count(), 1)   #จะเช็คว่ามีการซื้อแพ็คเกจแล้วจริงๆ
        
    def test_packbuy(self):
        self.c = Client()
        self.c.login(username='test', password='test')
        response = self.c.post(reverse('doctors:packbuy'), follow=True)
=======
    def test_packbuy(self):
        self.c = Client()
        response = self.c.get(reverse('doctors:packbuy'), follow=True)
        self.assertEqual(response.status_code, 200)
    
    def test_buy(self):
        self.c = Client()
        self.c.login(username='test', password='test')
        package1 = Package.objects.first()
        response = self.c.get(reverse('doctors:buy', args=(str(package1.id),)), follow=True)
        self.assertEqual(response.status_code, 200)

    def test_mypack(self):
        self.c = Client()
        self.c.login(username='test', password='test')
        response = self.c.get(reverse('doctors:mypack'), follow=True)
>>>>>>> Stashed changes
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'doctors/packbuy.html', 'doctors/layout.html')
        
    # not work
    # def test_mypack(self):
    #     self.c = Client()
    #     self.c.login(username='test', password='test')
    #     package1 = Package.objects.create(name="Package_name", price=3000, desc="detail", cond="condition")
    #     Buy.objects.create(self.patient, package1, "NOT PAID")
    #     response = self.c.get(reverse('doctors:mypack'), follow=True)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'doctors/mypack.html', 'doctors/layout.html')

#can't do it 
#  def test_appointment_invalid(self):
#         self.c = Client()
#         self.c.login(username='test', password='test')
            
#         self.assertEqual(Appointment.objects.all().count(), 1)
#         doctor1 = Doctor.objects.first()
#         response = self.c.post(reverse('doctors:appointment', args=(str(doctor1.id),)), follow=True)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'doctors/addnews.html', 'doctors/layout.html')
    
    def test_profile(self):
        self.c = Client()
        self.c.login(username='test', password='test')
        # appointment = Appointment.objects.filter(Patient_id=self.c)   #อาจใช้เช็คว่าผู้ใช้ถูกคนหรือเปล่า
        response = self.c.get(reverse('doctors:profile'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'doctors/profile.html', 'doctors/layout.html')
  
    def test_login(self):
        self.c = Client()
        response = self.c.post(reverse('doctors:login'), {'username': "test", 'password': "test"}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'doctors/index.html', 'doctors/layout.html')

    def test_login_invalid(self):
        self.c = Client()
        response = self.c.post(reverse('doctors:login'), {'username': "test", 'password': "test1"}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'doctors/login.html', 'doctors/layout.html')

    def test_logout(self):
        c = Client()
        c.force_login(User.objects.first())
        response = c.get(reverse('doctors:logout'), follow=True)
        self.assertEqual(response.status_code, 200)
    
    def test_register(self):
        self.c = Client()
        response = self.c.post(reverse('doctors:register'), {'username': "test", 'email': "test@testtest.com", 'password1': "testtesttest", 'password2': "testtesttest"}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'doctors/register.html')
    

    def test_doctor(self):
        self.c = Client()
        response = self.c.get(reverse('doctors:doctor'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'doctors/doctor.html', 'doctors/layout.html')
    
    
    def test_doctor_one(self):
        self.c = Client()
        doctor1 = Doctor.objects.first()
        response = self.c.get(reverse('doctors:docprofile', args=(str(doctor1.id),)), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'doctors/docprofile.html', 'doctors/layout.html')
    
    def test_deleteDoc(self):
        self.c = Client()
        doctor1 = Doctor.objects.first()
        response = self.c.post(reverse('doctors:deleteDoc', args=(str(doctor1.id),)), follow=True)
        self.assertEqual(response.status_code, 200)

        