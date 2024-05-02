import requests
import json
import random
from django.conf import settings
from ..models import *

WEBPAY_SECRET = "579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C"
WEBPAY_ID = "597055555532"
WEBPAY_URL = "https://webpay3gint.transbank.cl/rswebpaytransaction/api/webpay/v1.2/transactions"


def crearTransaccion(user_id, direccion):
    # se crea la orden de compra

    datos = Carrito.objects.filter(
        user_id=user_id).order_by('-id').all()
    suma = 0
    for dato in datos:
        valor = dato.cantidad*dato.producto.precio
        suma = suma+valor

    try:
        orden = OrdenDeCompra.objects.filter(
            user_id=user_id).get()
    except OrdenDeCompra.DoesNotExist:
        orden = OrdenDeCompra.objects.create(
            user_id=user_id, suma=suma, direccion=direccion)

    buy_order = f"orden{orden.id}"
    session_id = str(random.randrange(1000000, 99999999))
    amount = suma
    ruta = "http://www.comercio.cl/webpay/retorno"
    endpoint = WEBPAY_URL
    payload = {
        "buy_order": buy_order,
        "session_id": session_id,
        "amount": amount,
        "return_url": ruta
    }
    cabeceros = {
        'content-type': 'application/json',
        'Tbk-Api-Key-Id': WEBPAY_ID, 'Tbk-Api-Key-Secret': WEBPAY_SECRET
    }
    response = requests.post(endpoint, json=payload, headers=cabeceros)
    print("\nENDPOINT RESPONSE\n")

    # response.status_code
    respuesta = json.loads(response.text)
    print(respuesta)
    # guardo el token recibido
    OrdenDeCompra.objects.filter(id=orden.id).update(
        token_ws=respuesta['token'])
    # retorno token y URL
    ruta = f"{respuesta['url']}{respuesta['token']}"
    # print("sadasdasd")
    return respuesta


def verificarTransaccion(token):
    endpoint = f"{WEBPAY_URL}/{token}"
    cabeceros = {'content-type': 'application/json',
                 'Tbk-Api-Key-Id': WEBPAY_ID, 'Tbk-Api-Key-Secret': WEBPAY_SECRET
                 }
    response = requests.put(endpoint, headers=cabeceros)
    # response.status_code
    respuesta = json.loads(response.text)
    print("\nRespuesta -> ", respuesta)
    if response.status_code == 200:

        return [
            respuesta['status'], respuesta['card_detail']['card_number'], respuesta['transaction_date']
        ]
    else:
        return ['vacio']
