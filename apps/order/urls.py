from . import views
from django.urls import path


app_name = "orders"

urlpatterns = [
    path("adicionar/", views.add_orders, name="add_orders"),
    path("", views.list_orders, name="list_orders"),
    path("editar/<int:id_order>/", views.edit_orders, name="edit_orders"),
    path("excluir/<int:id_order>/", views.delete_orders, name="delete_orders"),
]
