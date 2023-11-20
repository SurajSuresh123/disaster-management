# myapp/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CitizenUser, StaffUser

class CitizenUserCreationForm(UserCreationForm):
    class Meta:
        model = CitizenUser
        fields = ['name','phone','email','username','password1','password2']

class StaffUserCreationForm(UserCreationForm):
    class Meta:
        model = StaffUser
        fields = ['name','phone','email','position','staff_id','password1','password2']
