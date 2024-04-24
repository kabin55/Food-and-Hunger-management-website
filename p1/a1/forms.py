from django import forms  
from a1.models import info 
from a1.models import * 
from django.contrib.auth.forms import  UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Donation

class info2(forms.ModelForm):
    class Meta:
        model = info
        fields= ['name','email','msg']

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['name', 'email', 'amount', 'message']


class LogInForm(AuthenticationForm):
    class Meta:
        model = User
        fields=['username','password']
        
    
class SignupForms(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email','password1',"password2"]
        