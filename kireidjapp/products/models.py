from django.db import models
from products import Product

"""
Modelo "Producto": Este modelo tendría campos como nombre 
del producto, descripción, precio, stock y 
una imagen del producto.

Relaciones: Muchos a muchos con el modelo "Factura"
Un producto puede ser asociado a muchas facturas y una 
factura puede tener varios productos asociados.

"""

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(verbose_name="Descripcion del producto",blank=True, null=True, default='', help_text='Ingrese una breve descripción del producto.')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)    
    product_image = models.ImageField(upload_to='products/') # modificar ruta de guardado de imagen

    def is_in_stock(self):
        return self.stock > 0



