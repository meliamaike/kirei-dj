from django.db import models
from reservations import Reservation, Customer
from products import Product
from services import Service


"""
    Modelo "Pago": Este modelo tendría campos como monto, fecha, 
    forma de pago, y reserva de la cita asociada.Tendría relaciones:

    Uno a uno con el modelo "Cita"
    Uno a uno con el modelo "Factura"
"""
    
class Payment(models.Model):
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=255)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)

"""
    Modelo "Factura": Este modelo tendría campos como fecha, 
    cliente asociado, los productos comprados y 
    servicios comprados, y el monto total.
"""

class Bill(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    services = models.ManyToManyField(Service)
    total_amount = models.DecimalField(max_digits=6, decimal_places=2)
