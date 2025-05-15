from django.shortcuts import render, redirect, get_object_or_404
from .forms import OrderForm
from .models import Order


def add_orders(request):
    template_name = 'order/add_orders.html'
    context = {}
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('orders:list_orders')
    form = OrderForm()
    context['form'] = form
    return render(request, template_name, context)


def list_orders(request):
    template_name = "order/list_orders.html"
    orders = Order.objects.filter()
    context = {"orders": orders}
    return render(request, template_name, context)



def edit_orders(request, id_order):
    template_name = "order/add_orders.html"
    context = {}
    order = get_object_or_404(Order, id=id_order)

    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect("orders:list_orders")
    form = OrderForm(instance=order)
    context["form"] = form
    return render(request, template_name, context)


def delete_orders(request, id_order):
    product = Order.objects.get(id=id_order)
    product.delete()
    return redirect("orders:list_orders")
