from django.urls import path
from .views import carro_webpay, carro_webpay_respuesta

urlpatterns = [
  path('webpay', carro_webpay.as_view(), name="carro_webpay"),
	path('webpay-respuesta', carro_webpay_respuesta.as_view(), name="carro_webpay_respuesta"),
]