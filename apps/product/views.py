from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm
from .models import Product


def add_products(request):
    template_name = 'product/add_products.html'
    context = {}
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('products:list_products')
    form = ProductForm()
    context['form'] = form
    return render(request, template_name, context)


def list_products(request):
    template_name = "product/list_products.html"
    products = Product.objects.filter()
    context = {"products": products}
    return render(request, template_name, context)


def edit_products(request, id_product):
    template_name = "product/add_products.html"
    context = {}
    product = get_object_or_404(Product, id=id_product)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("products:list_products")
    form = ProductForm(instance=product)
    context["form"] = form
    return render(request, template_name, context)


def delete_products(request, id_product):
    product = Product.objects.get(id=id_product)
    product.delete()
    return redirect("products:list_products")
