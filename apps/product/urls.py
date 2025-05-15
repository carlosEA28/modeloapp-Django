from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('adicionar/', views.add_products, name='add_products'),
    path("", views.list_products, name="list_products"),
    path("editar/<int:id_product>/", views.edit_products, name="edit_products"),
    path("excluir/<int:id_product>/", views.delete_products, name="delete_products"),
]