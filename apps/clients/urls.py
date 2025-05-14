from . import views
from django.urls import path


app_name = "clients"

urlpatterns = [
    path("adicionar/", views.add_clients, name="add_client"),
]
