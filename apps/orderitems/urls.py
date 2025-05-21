from django.urls import path
from . import views

app_name = 'orderitems'

urlpatterns = [
    path('adicionar/', views.add_orderitems, name='add_orderitems'),
    path("", views.list_orderitems, name="list_orderitems"),
    path("editar/<int:id_orderitem>/", views.edit_orderitems, name="edit_orderitems"),
    path("excluir/<int:id_orderitem>/", views.delete_orderitems, name="delete_orderitems"),
]
