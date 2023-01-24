from django.db import models
from django.utils import timezone
from . import ShoppingCart
from services import Service
from products import Product
from professionals import Professional
from payments import Payment
from customers import Customer


class Reservation(models.Model):
    shopping_cart = models.OneToOneField(ShoppingCart, on_delete=models.CASCADE, blank=False, null=False)
    date_time = models.DateTimeField()
    payment = models.OneToOneField(Payment, on_delete=models.CASCADE, blank=True, null=True)
    RESERVATION_STATUS = (
    ('pending', 'Pendiente de pago'),
    ('confirmed', 'Confirmado'),
    ('cancelled', 'Cancelado'),
    ('completed', 'Completado'),
)
    status = models.CharField(max_length=255, choices=RESERVATION_STATUS)

class ShoppingCart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='ShoppingCartProduct', through_fields=('shopping_cart','product'))
    services = models.ManyToManyField(Service, through='ShoppingCartServiceDetail', through_fields=('shopping_cart','service'))
    total_amount = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

class ShoppingCartProduct(models.Model):
    shopping_cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

class ShoppingCartServiceDetail(models.Model):
    shopping_cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    professional = models.ForeignKey(Professional,on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now, help_text="DD-MM-AAAA")

    #Cambiar cada 15 minutoss
    TIMESLOT_LIST = (
        (1, "10:00 - 11:00"),
        (2, "11:00 - 12:00"),
        (3, "12:00 - 13:00"),
        (4, "13:00 - 14:00"),
        (5, "14:00 - 15:00"),
        (6, "15:00 - 16:00"),
        (7, "16:00 - 17:00"),
        (8, "17:00 - 18:00"),
        (9, "18:00 - 19:00"),
    )

    timeslot = models.IntegerField(
        null=True,
        choices=TIMESLOT_LIST,
        default="Elija el horario",
    )

