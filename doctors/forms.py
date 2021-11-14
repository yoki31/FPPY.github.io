from django import forms
from django.db.models import fields
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.admin.widgets import  AdminDateWidget, AdminTimeWidget, AdminSplitDateTime
from .models import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CreateArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['header', 'doctor', 'context', 'img']


class CreateNewsForm(ModelForm):
    class Meta:
        model = New
        fields = ['header', 'context', 'img']

class accForm(ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        exclude = ['user', 'date_created']

class CreatePackageForm(ModelForm):
    class Meta:
        model = Package
        fields = '__all__'
        exclude = ['date_created']
        
class CreateDocForm(ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'
        exclude = ['date_created']

class StatusBuy(ModelForm):
    class Meta:
        model = Buy
        fields = ['status']

class SendSlip(ModelForm):
    class Meta:
        model = Buy
        fields = ['img']
        

# class CreateAppointmentForm(ModelForm):
#     class Meta:
#         model = Appointment
#         fields = '__all__'
#         exclude = ['Patient_id', 'Doctor_id']



class AppointmentForm(forms.Form):
    # your_name = forms.CharField(max_length=64)
    symptom = forms.CharField(max_length=100)
    date_input = forms.DateField(widget=AdminDateWidget())
    # time_input = forms.DateField(widget=AdminTimeWidget())
    # date_time_input = forms.DateField(widget=AdminSplitDateTime())