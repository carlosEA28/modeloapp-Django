from django import forms
from clientsocialnetworks.models import ClientSocialNetwork


class ClientSocialNetworkForm(forms.ModelForm):

    class Meta:
        model = ClientSocialNetwork
        exclude = ()
