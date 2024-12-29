from django.urls import path
from . import views

urlpatterns = [
    path('articulos/', views.articulos, name='listar_articulos'),
    path('categorias/<int:category_id>', views.category, name='categorias'),
    path('articulo_solo/<int:articulo_id>', views.articulo, name='articulo_solo')

]
