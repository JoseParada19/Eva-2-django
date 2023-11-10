from django.contrib import admin
from django.urls import path
from firstApp import views

app_name = 'firstApp'

urlpatterns = [
    path('admin/', admin.site.urls),
    path("clientes/",views.lista_cliente,name='clientes'),
    path('',views.vista_principal,name='principal'),
    path("registrar_cliente/",views.registrar_cliente,name='registrar_cliente'),
    path("editar_cliente/<int:id>",views.editar_cliente, name='editar_cliente'),
    path("eliminar_cliente/<int:id>",views.eliminar_cliente, name='eliminar_cliente'),

]



