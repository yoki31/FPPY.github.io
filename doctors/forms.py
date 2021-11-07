from django import forms
from django.db.models import fields
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
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