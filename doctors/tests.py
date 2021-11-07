from django.db.models.aggregates import Count
from django.http import response
from django.test import TestCase, Client
from django.urls import reverse
from .models import *
from .forms import *
from django.contrib.auth.models import User, Group
from django.contrib.auth.hashers import make_password
# Create your tests here.
class TestCase(TestCase):
    
    def setUp(self):
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

        """"setUp Models.py"""

        password = make_password('user123456')
        user = User.objects.create(username="user", password=password)
        patient = Patient.objects.create(user=user, First_name="Fname", Last_name="Lname", email= "user@example.com", phone="0987654321")
        
        doctorT = Doctor.objects.create(First_name="DFname", Last_name="DLname", email="doc@example.com", phone="0999999999")
        article = Article.objects.create(doctor=doctorT, header="Test", context="Lorem")
        news = New.objects.create(header="TestNews", context="Lorem20")
        #ข้ามการบริจาคไว้
        package = Package.objects.create(name="Package_name", price=3000, desc="detail", cond="condition")
        #ข้ามSpecialitie
        # appointment = Appointment.objects.create(Patient_id=patient, Doctor_id=doctor, symptom="Lorem10")#ไม่ชัวร์
        #ข้ามBuy

    def test_patient_exists(self):
        count_patient = Patient.objects.all().count()
        self.assertEqual(count_patient, 2)
        self.assertNotEqual(count_patient, 0)

    def test_doctor_exists(self):
        count_doctor = Doctor.objects.all().count()
        self.assertEqual(count_doctor, 1)
        self.assertNotEqual(count_doctor, 0)

    def test_article_exists(self):
        count_article = Article.objects.all().count()
        self.assertEqual(count_article, 1)
        self.assertNotEqual(count_article, 0)

    def test_news_exists(self):
        count_news = New.objects.all().count()
        self.assertEqual(count_news, 1)
        self.assertNotEqual(count_news, 0)

    def test_package_exists(self):
        count_package = Package.objects.all().count()
        self.assertEqual(count_package, 1)
        self.assertNotEqual(count_package, 0)

    # def test_appointment_exists(self):
    #     count_appointment = Appointment.objects.all().count()
    #     self.assertEqual(count_appointment, 1)
    #     self.assertNotEqual(count_appointment, 0)

    def test_str_patient(self):
        obj = Patient.objects.first()
        self.assertEqual(str(obj), obj.First_name)

    def test_str_doctor(self):
        obj = Doctor.objects.first()
        self.assertEqual(str(obj), obj.First_name)

    def test_str_article(self):
        obj = Article.objects.first()
        self.assertEqual(str(obj), obj.header)

    def test_str_news(self):
        obj = New.objects.first()
        self.assertEqual(str(obj), obj.header)

    #ข้ามการบริจาคไว้

    def test_str_package(self):
        obj = Package.objects.first()
        self.assertEqual(str(obj), obj.name)

    #ข้ามSpecialitie

    #ข้ามหมอ งงที่ฟิวเขียน

    #ข้ามBuy

    """
    ==================================================
    หมดช่วง test models
    ==================================================
    """

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
        
    def test_healthblog(self):
        self.c = Client()
        response = self.c.get(reverse('doctors:healthblog'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'doctors/healthblog.html', 'doctors/layout.html')
        
    def test_requirement(self):
        self.c = Client()
        response = self.c.get(reverse('doctors:project_requirement'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'doctors/requirement.html', 'doctors/layout.html')

    def test_healthblog_one(self):
        self.c = Client()
        response = self.c.get(reverse('doctors:healthblog'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'doctors/healthblog.html', 'doctors/layout.html')

    def test_healthblog(self):
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

    def test_deleteArticle(self):
        self.c = Client()
        article1 = Article.objects.first()
        response = self.c.post(reverse('doctors:deleteArticle', args=(str(article1.id),)), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'doctors/healthblog.html', 'doctors/layout.html')
        
    # def test_newscontent(self):
    #     self.c = Client()
    #     news1 = New.objects.first()
    #     response = self.c.get(reverse('doctors:news_content', args=(str(news1.id),)), follow=True)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'doctors/news_one.html', 'doctors/layout.html')

    # def test_deletenews(self):
    #     self.c = Client()
    #     news1 = New.objects.first()
    #     response = self.c.post(reverse('doctors:deleteNews', args=(str(news1.id),)), follow=True)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'doctors/news.html', 'doctors/layout.html')
        