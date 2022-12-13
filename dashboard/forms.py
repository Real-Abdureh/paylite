from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Transaction



class SelectCustomerForm(forms.ModelForm):
    class meta:
      model = Transaction
      fields = ['select']
