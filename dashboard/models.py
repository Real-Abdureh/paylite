from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from user.models import Profile


SCHOOLS = Profile.school


class Transaction(models.Model):
  select = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
  Name = models.CharField(max_length=200, null= True )
  Service = models.CharField(max_length=200, null= True)
  Amount = models.IntegerField(null = True)
  


# Create your models here.
