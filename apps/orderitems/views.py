from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from .forms import OrderItemForm
from .models import OrderItem

def add_orderitems(request):
    template_name = 'orderitems/add_orderitems.html'
    context = {}
    if request.method == 'POST':
        form = OrderItemForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('orderitems:list_orderitems')
    form = OrderItemForm()
    context['form'] = form
    return render(request, template_name, context)

def list_orderitems(request):
    template_name = "orderitems/list_orderitems.html"
    orderitems = OrderItem.objects.filter()
    context = {"orderitems": orderitems}
    return render(request, template_name, context)

def edit_orderitems(request, id_orderitem):
    template_name = "orderitems/add_orderitems.html"
    context = {}
    orderitem = get_object_or_404(OrderItem, id=id_orderitem)

    if request.method == "POST":
        form = OrderItemForm(request.POST, instance=orderitem)
        if form.is_valid():
            form.save()
            return redirect("orderitems:list_orderitems")
    form = OrderItemForm(instance=orderitem)
    context["form"] = form
    return render(request, template_name, context)

def delete_orderitems(request, id_orderitem):
    orderitem = OrderItem.objects.get(id=id_orderitem)
    orderitem.delete()
    return redirect("orderitems:list_orderitems")