from django.shortcuts import render, redirect

from clients.forms import ClientForm


# Create your views here.


def add_clients(request):
    template_name = "client/add_client.html"
    context = {}
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():  # Corrigido o erro aqui
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect(
                "categories:list_categories"
            )  # Corrigido o nome da URL aqui
    form = ClientForm()
    context["form"] = form
    return render(request, template_name, context)
