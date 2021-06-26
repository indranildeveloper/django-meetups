from django import forms
from django.db.models import fields

# from .models import Participant


# class RegistrationForm(forms.ModelForm):
#     class Meta:
#         model = Participant
#         fields = ['email']

class RegistrationForm(forms.Form):
    email = forms.EmailField(label='Your Email')
