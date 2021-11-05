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
        fields = '__all__'
        
        
class CreateNewsForm(ModelForm):
    class Meta:
        model = New
        fields = '__all__'