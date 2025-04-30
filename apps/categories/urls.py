from django.urls import path
from . import views

app_name = "categories"

urlpatterns = [
    path("adicionar/", views.add_Category, name="add_Category"),
]
