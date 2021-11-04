from django import forms
from django.db.models import fields
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Articles, News 

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
        
class CreateArticleForm(ModelForm):
    class Meta:
        model = Articles
        fields = '__all__'
        
        
class CreateNewsForm(ModelForm):
    class Meta:
        model = News
        fields = '__all__'