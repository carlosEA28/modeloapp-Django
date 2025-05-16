from django.db import models

class SocialNetwork(models.Model):
    name = models.CharField('Nome', max_length=100)
    description = models.TextField('Descrição')

    class Meta:
        verbose_name = 'Rede Social'
        verbose_name_plural = 'Redes Sociais'
        ordering = ['name']

    def __str__(self):
        return self.name
