from django.db import models
import uuid
from django.contrib.auth.models import User


class Transaction(models.Model):
  select = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
  Name = models.CharField(max_length=200, null= True )
  Service = models.CharField(max_length=200, null= True)
  Amount = models.IntegerField(null = True)
  # refrence = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True)

  def __str__(self):
        return f'{self.select.username}-Transaction'
  


# Create your models here.
