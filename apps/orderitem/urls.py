from django.urls import path
from . import views

app_name = 'orderitems'

urlpatterns = [
    path('adicionar/', views.add_orderitems, name='add_orderitems'),
    path("", views.list_orderitems, name="list_orderitems"),
    path("editar/<>/", views.edit_orderitems, name="edit_orderitems"),
    path("excluir/<>/", views.delete_orderitems, name="delete_orderitems"),
]