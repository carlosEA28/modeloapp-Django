from . import views
from django.urls import path


app_name = "clientsocialnetworks"

urlpatterns = [
    path('', views.list_clientsocialnetwork, name='list_clientsocialnetwork'),
    path('adicionar/', views.add_clientsocialnetwork, name='add_clientsocialnetwork'),
    path('editar/<int:id_clientsocialnetwork>/', views.edit_clientsocialnetwork, name='edit_clientsocialnetwork'),
    path('excluir/<int:id_clientsocialnetwork>/', views.delete_clientsocialnetwork, name='delete_clientsocialnetwork'),
]
