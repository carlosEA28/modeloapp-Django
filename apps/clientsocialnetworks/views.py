from django.shortcuts import render, redirect, get_object_or_404
from clientsocialnetworks.models import ClientSocialNetwork
from clientsocialnetworks.forms import ClientSocialNetworkForm

def add_clientsocialnetwork(request):
    template_name = 'clientsocialnetworks/add_clientsocialnetwork.html'
    context = {}
    if request.method == 'POST':
        form = ClientSocialNetworkForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('clientsocialnetworks:list_clientsocialnetwork')
    form = ClientSocialNetworkForm()
    context['form'] = form
    return render(request, template_name, context)

def list_clientsocialnetwork(request):
    template_name = "clientsocialnetworks/list_clientsocialnetwork.html"
    clientsocialnetwork = ClientSocialNetwork.objects.filter()
    context = {"clientsocialnetwork": clientsocialnetwork}
    return render(request, template_name, context)

def edit_clientsocialnetwork(request, id_clientsocialnetwork):
    template_name = 'clientsocialnetworks/add_clientsocialnetwork.html'
    context = {}
    csn = get_object_or_404(ClientSocialNetwork, id=id_clientsocialnetwork)

    if request.method == 'POST':
        form = ClientSocialNetworkForm(request.POST, instance=csn)
        if form.is_valid():
            form.save()
            return redirect('clientsocialnetworks:list_clientsocialnetwork')
    form = ClientSocialNetworkForm(instance=csn)
    context['form'] = form
    return render(request, template_name, context)

def delete_clientsocialnetwork(request, id_clientsocialnetwork):
    csn = get_object_or_404(ClientSocialNetwork, id=id_clientsocialnetwork)
    csn.delete()
    return redirect('clientsocialnetworks:list_clientsocialnetwork')

