from django.urls import path
from . import views

app_name ="pedidos"
urlpatterns = [
    path('', views.home, name='home'),
    path('cliente/', views.cliente, name='cliente'),
    path('mesero/', views.mesero, name='mesero'),
    path('comida/', views.comida, name='comida'),
    path('comida/<str:categoria>/', views.detalle_comida, name='detalle_comida'),
    path('bebidas/', views.bebidas, name='bebidas'),
    path('detalle_bebidas/<str:categoria>/', views.detalle_bebida, name='detalle_bebida'),
    path('editar_orden/', views.editar_orden, name='editar_orden'),
    
]
