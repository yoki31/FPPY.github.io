from django.db.models.aggregates import Count
from django.http import response
from django.test import TestCase, Client
from django.urls import reverse
from .models import *
from .forms import *
from django.contrib.auth.models import User, Group
from django.contrib.auth.hashers import make_password
import datetime
# Create your tests here.
class TestCase(TestCase):
    
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


    def test_patient_exists_str(self):
        count_patient = Patient.objects.all().count()
        self.assertEqual(str(Patient.objects.get(First_name="Fname" )), 'Fname')
        self.assertEqual(count_patient, 1)
        self.assertNotEqual(count_patient, 0)

    def test_doctor_exists_str(self):
        count_doctor = Doctor.objects.all().count()
        obj = Doctor.objects.first()
        self.assertEqual(str(obj), obj.First_name)
        self.assertEqual(count_doctor, 1)
        self.assertNotEqual(count_doctor, 0)

    def test_article_exists_str(self):
        count_article = Article.objects.all().count()
        obj = Article.objects.first()
        self.assertEqual(str(obj), obj.header)
        self.assertEqual(count_article, 1)
        self.assertNotEqual(count_article, 0)

    def test_news_exists_str(self):
        count_news = New.objects.all().count()
        obj = New.objects.first()
        self.assertEqual(str(obj), obj.header)
        self.assertEqual(count_news, 1)
        self.assertNotEqual(count_news, 0)

    def test_package_exists_str(self):
        count_package = Package.objects.all().count()
        obj = Package.objects.first()
        self.assertEqual(str(obj), obj.name)
        self.assertEqual(count_package, 1)
        self.assertNotEqual(count_package, 0)

    def test_appointment_str(self):
        obj = Appointment.objects.first()
        self.assertEqual(str(obj), f'{obj.Doctor_id.First_name} > {obj.Patient_id.First_name}')

    def test_buy_str(self):
        obj = Buy.objects.first()
        self.assertEqual(str(obj), f'{obj.patient.First_name} >>> {obj.package}')

