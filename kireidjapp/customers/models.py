from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

class Customer(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    DOCUMENT_TYPE = (
    ('dni', 'DNI'),
    ('cuit', 'CUIT'),
    ('cuil', 'CUIL'),
)
    document_type = models.CharField(max_length=30, choices=DOCUMENT_TYPE)
    document_number = models.CharField(max_length=30)
    email = models.EmailField(max_length=255, unique=True)
    country_code = models.CharField(max_length=5)
    area_code = models.CharField(max_length=5)
    phone_number = PhoneNumberField()
    password = models.PasswordField()
    password_confirmation = models.PasswordField()
    profile_image = models.ImageField(upload_to='customers/') # modificar ruta de guardado de imagen
