from django import forms
from django.utils.translation import gettext_lazy as _ 

class EmployeeForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    department = forms.CharField()