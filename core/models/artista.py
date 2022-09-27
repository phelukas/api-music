from django.db import models
from django.utils.translation import gettext_lazy as _


class Artista(models.Model):

    nome = models.CharField("Nome", null=False, max_length=200, blank=False)
    quantidade_musicas = models.IntegerField(
        "Quantidade de musicas", null=True, blank=True, default=0)

    class Meta:
        verbose_name = _("Artista")
        verbose_name_plural = _("Artistas")

    def __str__(self):
        return self.nome
