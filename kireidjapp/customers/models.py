from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

class Customer(AbstractUser):
    phone_number = PhoneNumberField()
    #phone_number = models.CharField(max_length=20)