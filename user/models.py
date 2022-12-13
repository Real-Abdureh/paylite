from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    staff = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    school = models.CharField(max_length=200, null=True)
    phone = models.IntegerField( null=True)
    address = models.CharField(max_length=200, null=True)
    Bank = models.CharField(max_length=200, null=True)
    Account= models.IntegerField( null=True)
    logo = models.ImageField(default='default.png',
                              upload_to='profile_images', null=True)
    licenses = models.ImageField(default='default.png',
                              upload_to='profile_images', null=True)
    cac = models.ImageField(default='default.png',
                              upload_to='profile_images', null=True)

    def __str__(self):
        return f'{self.staff.username}-Profile'