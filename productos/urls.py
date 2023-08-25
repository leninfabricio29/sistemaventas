from django.urls import path
from .views import view_productos, registrar_producto

urlpatterns = [
    path('list/', view_productos, name='page-list-productos'),
    path('add-product/',registrar_producto, name="page-nuevo-producto")
]
