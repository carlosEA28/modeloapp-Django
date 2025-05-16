from django.db import models
from socialnetworks.models import SocialNetwork
from clients.models import Client

# Create your models here.

class ClientSocialNetwork(models.Model):
     
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    socialnetwork = models.ForeignKey(SocialNetwork, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Cliente Rede Social'
        verbose_name_plural = 'Cliente Redes Sociais'
        #ordering =['-client__id']