from django.db import models
from django.contrib.auth.models import AbstractUser

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField
from django_countries import countries

# Create your models here.
class CustomUser(AbstractUser):
    # add additional fields in here
    photo = models.ImageField(upload_to="profilepic", 
        null=True, 
        blank=True,)
    birthday = models.DateTimeField(null=True, blank=True, default='2000-01-01')
    country = CountryField(choices=list(countries),default='Taiwan')
    city = models.CharField(max_length=100, default='', blank=True)
    count_mail = models.IntegerField(default=0)
    count_friend = models.IntegerField(default=0)
    GENDER_CHOICES = (('M', 'Male'),('F', 'Female'),)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')

    def __str__(self):
        return self.email