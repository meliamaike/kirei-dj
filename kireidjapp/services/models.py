from django.db import models

"""
Aplicación "Servicios":

    Modelo "Servicio": Este modelo tendría campos como 
    nombre del servicio, descripción, precio y duración.
Relaciones:
    Muchos a muchos con el modelo "Cita"
    Un servicio puede ser asociado a muchas citas, 
    y una cita puede tener muchos servicios asociados.
"""

class Service(models.Model):
    service = models.CharField(max_length = 200)
    description = models.TextField(verbose_name="Product Description")
    duration = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.service
    
    
