from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('adicionar/', views.add_products, name='add_products'),
]