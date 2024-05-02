from django.db import models
from django.contrib.auth.models import User


class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    precio = models.PositiveIntegerField(default=0)
    stock = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'producto'


# carrito
class Carrito(models.Model):
    producto = models.ForeignKey(Producto, models.DO_NOTHING)
    user = models.ForeignKey(User, models.DO_NOTHING, default=1)
    cantidad = models.PositiveIntegerField(default=0)
    fecha = models.DateField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return f"{self.producto.nombre}"

    class Meta:
        db_table = 'carrito'


class OrdenDeCompra(models.Model):
    user = models.ForeignKey(
        User, models.DO_NOTHING, default=1)
    token_ws = models.CharField(max_length=255, default='0')
    tarjeta = models.CharField(max_length=10, default='0')
    fecha_transbank = models.CharField(max_length=100, default='0')
    estado_transbank = models.CharField(max_length=100, default='0')
    suma = models.PositiveIntegerField(default=0)
    direccion = models.TextField(default='0')
    observaciones = models.TextField(default='')
    fecha = models.DateField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return f"N°{self.id}"

    class Meta:
        db_table = 'orden_de_compra'


class OrdenDeCompraDetalle(models.Model):
    orden_de_compra = models.ForeignKey(OrdenDeCompra, models.DO_NOTHING)
    producto = models.ForeignKey(Producto, models.DO_NOTHING, default=1)
    cantidad = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"N°{self.id}"

    class Meta:
        db_table = 'orden_de_compra_detalle'
