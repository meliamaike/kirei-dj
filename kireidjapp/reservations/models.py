import datetime
from django.db import models
from django.utils import timezone

"""
Modelo "Appointment": Este modelo tendría campos como fecha y 
hora de la cita, servicio solicitado, profesional asignado, 
cliente asociado y estado de la cita (por ejemplo, confirmada, 
cancelada, etc.)
Tendría relaciones:

    Uno a muchos con el modelo "Servicio" y con "Profesional" porque 1 cita puede tener varios servicios y varios profesionales a cargo.
    Uno a uno con el modelo "Cliente" porque 1 cita tiene 1 cliente.
"""
#class Appointment(models.Model):
    #date = models.DateTimeField("dia de la cita")



"""
Modelo "Schedule": Este modelo tendría campos como hora de inicio y 
fin, día de la semana y profesional asociado. 
Sirve para definir el horario disponible de los profesionales 
para atender citas.
Tendría relaciones:
Uno a muchos: La relación entre el Modelo "Horario" y el Modelo "Profesional", ya que un profesional puede tener varios horarios de disponibilidad.

Muchos a uno: La relación entre el Modelo "Horario" y el Modelo "Día de la semana", ya que varios horarios pueden corresponder a un mismo día de la semana.

Muchos a muchos: La relación entre el Modelo "Horario" y el Modelo "Appointment", ya que si un profesional tiene varios horarios disponibles para atender citas y una cita puede ser programada en varios horarios, entonces se requeriría una relación muchos a muchos entre ambos modelos.




"""
#class Schedule(models.Model):

