from django import forms
from django.core import validators
from crudapp.models import UserData

class crudForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone_number = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    v_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

# alterative
# class crudForm(forms.ModelForm):
#     class Meta:
#         model = UserData
#         fields = '__all__'


