from django.shortcuts import render, redirect, get_object_or_404
from .forms import SocialNetworkForm
from .models import SocialNetwork

def add_socialnetwork(request):
    template_name = 'socialnetworks/add_socialnetwork.html'
    context = {}
    if request.method == 'POST':
        form = SocialNetworkForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('socialnetworks:list_socialnetwork')
    form = SocialNetworkForm()
    context['form'] = form
    return render(request, template_name, context)


def list_socialnetwork(request):
    template_name = "socialnetworks/list_socialnetwork.html"
    redes = SocialNetwork.objects.filter()
    context = {"redes": redes}
    return render(request, template_name, context)


def edit_socialnetwork(request, id_socialnetwork):
    template_name = "socialnetworks/add_socialnetwork.html"
    context = {}
    rede = get_object_or_404(SocialNetwork, id=id_socialnetwork)

    if request.method == "POST":
        form = SocialNetworkForm(request.POST, instance=rede)
        if form.is_valid():
            form.save()
            return redirect("socialnetworks:list_socialnetwork")
    form = SocialNetworkForm(instance=rede)
    context["form"] = form
    return render(request, template_name, context)


def delete_socialnetwork(request, id_socialnetwork):
    rede = get_object_or_404(SocialNetwork, id=id_socialnetwork)
    rede.delete()
    return redirect("socialnetworks:list_socialnetwork")
