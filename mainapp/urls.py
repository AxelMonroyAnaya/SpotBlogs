from django.urls import path
from . import views as vw
urlpatterns = [
    path('', vw.index, name='index'),
    path('inicio/', vw.index, name='index'),
    path('registro1/', vw.registro, name='registro'),
    path('sesion/', vw.sesion, name='login'),
    path('cerrar_sesion/', vw.cerrar_sesion, name='logout'),
]
