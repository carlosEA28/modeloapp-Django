from django.shortcuts import render

from apps.client.forms import ClientForm

# Create your views here.


def add_Cient(request):
    template_name = "client/add_client.html"
    context = {}

    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            f.save_m2m()
            return redirect(
                "categories:list_categories"
            )  # fazer a tela com as infos do cliente

        form = CategoryForm()
        context["form"] = form
        return render(request, template_name, context)
