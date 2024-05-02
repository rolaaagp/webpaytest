from django.contrib import admin
from . import models

admin.site.register(models.Producto)
admin.site.register(models.Carrito)
admin.site.register(models.OrdenDeCompra)
admin.site.register(models.OrdenDeCompraDetalle)
