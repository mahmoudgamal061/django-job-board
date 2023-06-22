from django import forms
from django.contrib.auth.forms import User 
from django.contrib.auth.forms import UserCreationForm 


class SignupForm(UserCreationForm):
    class meta:
        model = User
        fields ='__all__'
        