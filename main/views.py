from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_list_or_404
from .utilidades import webpay
from .models import *


# def carro_pagar(request):
#     cuantos = Carrito.objects.filter(
#         user_id=request.session['user_id']).count()

#     datos = Carrito.objects.filter(
#         user_id=request.session['user_id']).order_by('-id').all()

#     suma = 0
#     for dato in datos:
#         valor = dato.cantidad*dato.producto.precio
#         suma = suma+valor
#     usuario = UsersMetadata.objects.filter(
#         id=request.session['users_metadata_id']).get()
#     comunas = Comuna.objects.all()
#     return render(request, 'carro/pagar.html', {'datos': datos, 'suma': suma, 'usuario': usuario, 'comunas': comunas, 'cuantos': cuantos})


class carro_webpay(APIView):
    def post(self, request):
        try:
            direccion = request.data['direccion']
            result = webpay.crearTransaccion(
                request.data['user_id'], direccion
            )
            return Response({'url': result['url'], 'token': result['token']})
        except Exception as e:
            print(e)
            return Response({"error": str(e)})


class carro_webpay_respuesta(APIView):
    def get(self, request):

        if not request.data.get('token_ws'):
            return Response("error, no hay token webpay")
        token = request.data.get('token_ws')
        result = webpay.verificarTransaccion(token)

        if result[0] == 'vacio':
            print("\nResult -> ", result)
            return Response("error, la transacción falló.")
        if result[0] == 'AUTHORIZED':
            try:
                orden = OrdenDeCompra.objects.filter(
                    user_id=request.data['user_id'], estado_id=3).get()
            except OrdenDeCompra.DoesNotExist:
                return Response("error, no hay ordenes de compra.")
            OrdenDeCompra.objects.filter(
                user_id=request.session['user_id'], estado_transbank=0).update(

                token_ws=token, estado_transbank=result[0], fecha_transbank=result[2], tarjeta=result[1]
            )
            suma = 0
            datos = Carrito.objects.filter(
                user_id=request.session['user_id']).all()

            for dato in datos:
                valor = dato.cantidad*dato.producto.precio
                suma = suma+valor

                OrdenDeCompraDetalle.objects.create(
                    orden_de_compra_id=orden.id, producto_id=dato.producto_id, cantidad=dato.cantidad
                )

            Carrito.objects.filter(user_id=request.session['user_id']).delete()

            return Response("siga a la siguiente url: localhost:5173/etc")
        if result[0] == 'FAILED':
            OrdenDeCompra.objects.filter(
                user_id=request.session['user_id']).filter(estado_transbank=0).update(
                token_ws=token, fecha_transbank=result[2], tarjeta=result[1], estado_id=5
            )

            return Response("error, no se pudo completar el pago, estado: FAILED.")
