from django.shortcuts import render, redirect
from .forms import CategoryForm
from .models import Category, models

# Create your views here.


def add_Category(request):
    template_name = "categories/add_category.html"
    context = {}
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():  # Corrigido o erro aqui
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect("core:home")  # Corrigido o nome da URL aqui
    form = CategoryForm()
    context["form"] = form
    return render(request, template_name, context)


def list_categories(request):
    template_name = "categories/list_categories.html"
    categories = Category.objects.filter()
    context = {"categories": categories}
    return render(request, template_name, context)
