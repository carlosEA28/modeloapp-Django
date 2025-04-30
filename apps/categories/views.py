from django.shortcuts import render, redirect
from .forms import CategoryForm
from .models import Category, models
from django.shortcuts import render, redirect, get_object_or_404

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


def edit_category(request, id_category):
    template_name = "categories/add_category.html"
    context = {}
    category = get_object_or_404(Category, id=id_category)

    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect("categories:list_categories")
    redirect("categories:list_categories")
    form = CategoryForm(instance=category)
    context["form"] = form
    return render(request, template_name, context)
