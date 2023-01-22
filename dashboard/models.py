from django.db import models
import uuid
from django.contrib.auth.models import User


class Transaction(models.Model):
  id = models.UUIDField(primary_key = True, default = uuid.uuid4)
  select = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
  Payer_Name = models.CharField(max_length=200, null= True )
  Payer_Phone_no = models.IntegerField(null = True)
  Payer_Email = models.EmailField(null=True)
  Service = models.CharField(max_length=200, null= True)
  Amount = models.IntegerField(null = True)
  Date = models.DateTimeField(auto_now_add= True)
  #refrence = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True)

  def __str__(self):
        return f'{self.select.username}-Transaction'
  


# Create your models here.
