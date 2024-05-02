from rest_framework.serializers import ModelSerializer
from . import models
from django.contrib.auth.models import User


class UserMS(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email',)


class ProductoMS(ModelSerializer):
    class Meta:
        model = models.Producto
        fields = '__all__'

# Carrito


class CarritoMS(ModelSerializer):
    producto = ProductoMS(read_only=True)
    user = UserMS(read_only=True)

    class Meta:
        model = models.Carrito
        fields = '__all__'


# OrdenDeCompra
class OrdenDeCompraMS(ModelSerializer):
    user = UserMS(read_only=True)

    class Meta:
        model = models.OrdenDeCompra
        fields = '__all__'

# OrdenDeCompraDetalle


class OrdenDeCompraDetalleMS(ModelSerializer):
    orden_de_compra = OrdenDeCompraMS(read_only=True)

    class Meta:
        model = models.OrdenDeCompraDetalle
        fields = '__all__'
