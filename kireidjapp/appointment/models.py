from django.db import models
from services import Service
from professionals import Professional
from customers import Customer
from availability import Availability

"""
Modelo "Appointment": Este modelo tendría campos como fecha y 
hora de la cita, servicio solicitado, profesional asignado, 
cliente asociado y estado de la cita (por ejemplo, confirmada, 
cancelada, etc.)
Tendría relaciones:

    Uno a muchos con el modelo "Servicio" y con "Profesional" porque 1 cita puede tener varios servicios y varios profesionales a cargo.
    Uno a uno con el modelo "Cliente" porque 1 cita tiene 1 cliente.
"""
class Appointment(models.Model):
    services = models.ManyToManyField(Service)    
    professional = models.ManyToManyField(Professional)
    availability_slot = models.ForeignKey(Availability, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    APPOINTMENT_STATUS = (
    ('confirmed', 'Confirmada'),
    ('cancelled', 'Cancelada'),
    ('pending', 'Pendiente'),
)
    status = models.CharField(max_length=20, choices=APPOINTMENT_STATUS)

