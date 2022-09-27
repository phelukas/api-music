from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models.musica import Musica


class Playlist(models.Model):

    nome = models.CharField("Nome", null=False, max_length=200, blank=False)
    musica = models.ManyToManyField(Musica)
    quantidade_musicas = models.IntegerField(
        "Quantidade de musicas", null=True, blank=True, default=0)
    duracao = models.FloatField("Duração", null=True, blank=True, default=0)

    class Meta:
        verbose_name = _("playlist")
        verbose_name_plural = _("playlists")

    def __str__(self):
        return self.nome
