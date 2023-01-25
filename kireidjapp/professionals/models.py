from django.db import models
from services import Service
from availability import AvailabilitySlot
"""
Modelo "Profesional": Este modelo tendría campos como nombre, 
información de contacto, servicio, horarios disponibles 
y la fecha en que comenzó a trabajar. 

"""

class Professional(models.Model):
    professional = models.CharField(max_length=255)
    services = models.ManyToManyField(Service)
    start_date = models.DateField()
    availability_slot = models.ManyToManyField(AvailabilitySlot)

    