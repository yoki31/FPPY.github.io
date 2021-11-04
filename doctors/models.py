from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# USER
class Patient(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    First_name = models.CharField(max_length=100, null = True)
    Last_name = models.CharField(max_length=100, null = True)
    email = models.CharField(max_length=200, null = True)
    Patient_id = models.CharField(max_length=10, null = True)
    profile_pic = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f"{self.Patient_id}: {self.First_name} {self.Last_name}"

class Doctor(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    First_name = models.CharField(max_length=100, null = True)
    Last_name = models.CharField(max_length=100, null = True)
    email = models.CharField(max_length=200, null = True)
    Doctor_id = models.CharField(max_length=10, null = True)

    def __str__(self):
        return f"{self.Doctor_id}: {self.First_name} {self.Last_name}"

#เบล็ดเตล็ด
class Articles(models.Model):
    Doctor_id = models.ForeignKey(Doctor, null = True, on_delete=models.CASCADE)
    header = models.CharField(max_length=150, null = True,)
    context = models.CharField(max_length=300, null = True,)

    def __str__(self):
        return f"{self.header} \n {self.context}"



class News(models.Model):
    Doctor_id = models.ForeignKey(Doctor, null = True, on_delete=models.CASCADE)
    header = models.CharField(max_length=150, null = True,)
    context = models.CharField(max_length=300, null = True,)


    def __str__(self):
        return f"{self.header} \n {self.context}"

class ProofDonation(models.Model): #ให้คนบริจาค กรอกเอง ต้องเชื่อมไหม
    First_nameWhoDonate = models.CharField(max_length=150, null = True,)
    Last_nameWhoDonate = models.CharField(max_length=150, null = True,)
    Howmuch = models.IntegerField(null=True,)
    dateDonate = models.DateTimeField(null=True,)


    def __str__(self):
        return f"{self} ({self.Howmuch}) \n {self.dateDonate}"

class Package(models.Model):
    Patient_id = models.OneToOneField(Patient, null=True, on_delete=models.CASCADE)
    name_package = models.CharField(max_length=150, null=True,)
    cost = models.IntegerField(null=True, )
    description = models.CharField(max_length=300, null=True,)
    condition = models.CharField(max_length=300, null=True,)


    def __str__(self):
        return f"{self.name_package} ({self.cost}) \n {self.description} \n {self.condition}"

# ข้าวหลามตัด

class Specialitie(models.Model):
    Patient_id = models.OneToOneField(Patient, null=True, on_delete=models.CASCADE)
    Doctor_id = models.OneToOneField(Doctor, null = True, on_delete=models.CASCADE)
    spec = models.CharField(max_length=100, null = True)

    def __str__(self):
        return f"{self.Patient_id} เลือก {self.spec} หมอมีดังนี้ {self.Doctor_id} "

class Appointment(models.Model):
    Patient_id = models.OneToOneField(Patient, null=True, on_delete=models.CASCADE)
    Doctor_id = models.OneToOneField(Doctor, null = True, on_delete=models.CASCADE)
    symptom = models.CharField(max_length=100, null = True)
    dateapp = models.DateTimeField(null=True,)

    def __str__(self):
        return f"หมอ {self.Patient_id} นัด {self.Patient_id} วัน {self.dateapp} "

class Buy(models.Model):
    Patient_id = models.OneToOneField(Patient, null=True, on_delete=models.CASCADE)
    name_package = models.OneToOneField(Package, null = True, on_delete=models.CASCADE)
    status =  models.BooleanField(default=True)
    # invoice ทำไง

    def __str__(self):
        return f"{self.Patient_id} ซื่อ {self.Patient_id} สถานะ {self.dateapp} "