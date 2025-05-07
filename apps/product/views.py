from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm
from .models import Product, models

# Create your views here.

def add_Product(request):
    template_name = "product/add_product.html"
    context = {}
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():  # Corrigido o erro aqui
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect(
                "categories:list_categories"
            )  # Corrigido o nome da URL aqui
    form = ProductForm()
    context["form"] = form
    return render(request, template_name, context)