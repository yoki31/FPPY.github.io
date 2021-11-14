from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


# USER
class Patient(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    First_name = models.CharField(max_length=100, blank=True, null = True)
    Last_name = models.CharField(max_length=100, null = True)
    phone = models.CharField(max_length=100, null = True)
    email = models.CharField(max_length=200, null = True)
    date_created = models.DateTimeField(default=timezone.now)
    profile_pic = models.ImageField(default='defaultpic.jpeg',null=True)

    def __str__(self):
        return self.First_name

class Doctor(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    First_name = models.CharField(max_length=100, blank=True, null = True)
    Last_name = models.CharField(max_length=100, null = True)
    phone = models.CharField(max_length=100, null = True)
    email = models.CharField(max_length=200, null = True)
    spec = models.CharField(max_length=100, null = True)
    date_created = models.DateTimeField(default=timezone.now)
    profile_pic = models.ImageField(default='person.jpg',null=True)

    def __str__(self):
        return self.First_name

#เบล็ดเตล็ด
class Article(models.Model):
    doctor = models.ForeignKey(Doctor, null = True, on_delete=models.CASCADE)
    header = models.CharField(max_length=150, null = True,)
    context = models.TextField()
    img = models.ImageField(default='pic.jpg', null=True)
    date_created = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.header

class New(models.Model):
    doctor = models.ForeignKey(Doctor, null = True, on_delete=models.CASCADE)
    header = models.CharField(max_length=150, null = True,)
    context = models.TextField()
    img = models.ImageField(default='pic.jpg', null=True)
    date_created = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.header

class Package(models.Model):
    name = models.CharField(max_length=100, null = True)
    price = models.IntegerField(null = True)
    desc =models.CharField(max_length=200, null = True)
    cond =models.CharField(max_length=200, null = True)
    img = models.ImageField(default='pic.jpg', null=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self) :
        return self.name

class Appointment(models.Model):
    Patient_id = models.ForeignKey(Patient, null=True, on_delete=models.CASCADE)
    Doctor_id = models.ForeignKey(Doctor, null = True, on_delete=models.CASCADE)
    symptom = models.CharField(max_length=100, null = True)
    dateapp = models.DateField(null=True,)

    def __str__(self):
        return f"{self.Doctor_id.First_name} > {self.Patient_id.First_name}"

class Buy(models.Model):
    STATUS = (
            ('NOT PAID', 'NOT PAID'),
            ('PAID', 'PAID'),
    )

    patient = models.ForeignKey(Patient, null=True, on_delete= models.CASCADE)
    package = models.ForeignKey(Package, null=True, on_delete= models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
    img = models.ImageField(default='nopic.png', null=True)
    status = models.CharField(max_length=200, null = True, choices=STATUS, default='NOT PAID')

    def __str__(self) :
        return f'{self.patient.First_name} >>> {self.package}'


