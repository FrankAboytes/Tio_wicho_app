from django.urls import path
from . import views
from .views import CustomLoginView
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage


app_name ="pedidos"
urlpatterns = [
    path('', views.home, name='home'),
    path('cliente/', views.cliente, name='cliente'),
    path('mesero/', views.mesero, name='mesero'),
    path('comida/', views.comida, name='comida'),
    path('comida/<str:categoria>/', views.detalle_comida, name='detalle_comida'),
    path('actualizar_cantidad/', views.actualizar_cantidad, name='actualizar_cantidad'),
    path('bebidas/', views.bebidas, name='bebidas'),
    path('detalle_bebida/<str:categoria>/', views.detalle_bebida, name='detalle_bebida'),
    path('editar_orden/', views.editar_orden, name='editar_orden'),
    path('resumen_pedido/', views.resumen_pedido, name='resumen_pedido'),
    path('iniciar_sesion_invitado/<str:mesa_id>/', views.iniciar_sesion_invitado, name='iniciar_sesion_invitado'),
    path('cerrar_sesion_invitado/<str:mesa_id>/', views.cerrar_sesion_invitado, name='cerrar_sesion_invitado'),
    path('editar_orden/', views.editar_orden, name='editar_orden'),  # Incluye las rutas de tu aplicación 'pedidos'
    path('accounts/login/', CustomLoginView.as_view(), name='login'),  # Ruta de inicio de sesión
    path('seleccionar_mesa/<str:mesa_id>/', views.seleccionar_mesa, name='seleccionar_mesa'),
    path('reiniciar_pedido/', views.reiniciar_pedido, name='reiniciar_pedido'),
    path('actualizar_cantidad_bebida/', views.actualizar_cantidad_bebida, name='actualizar_cantidad_bebida'),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('images/favicon.ico'))),
]
