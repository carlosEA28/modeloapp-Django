from django.urls import path
from . import views

app_name = "categories"

urlpatterns = [
    path("adicionar/", views.add_Category, name="add_category"),
    path("", views.list_categories, name="list_categories"),
    path("editar/<int:id_category>/", views.edit_category, name="edit_category"),
]
