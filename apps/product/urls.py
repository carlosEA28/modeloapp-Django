from django.urls import path
from . import views

app_name = "product"

urlpatterns = [
    path("adicionar/", views.add_Product, name="add_product"),
   
]
