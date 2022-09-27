from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models.artista import Artista


class Musica(models.Model):

    nome = models.CharField("Nome", null=False, max_length=200, blank=False)
    artista = models.ForeignKey(
        Artista, on_delete=models.CASCADE, related_name="musica")
    duracao = models.FloatField("Duração", null=False, blank=False)
    genero = models.CharField("Gênero", null=True, max_length=200, blank=True)

    class Meta:
        verbose_name = _("Musica")
        verbose_name_plural = _("Musicas")

    def __str__(self):
        return self.nome
