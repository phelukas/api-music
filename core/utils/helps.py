from core.models.artista import Artista
from core.models.playlist import Playlist
from core.models.musica import Musica


def add_musica_artista(artista_id):
    artista = Artista.objects.get(id=artista_id)
    artista.quantidade_musicas += 1
    artista.save()


def sub_musica_artista(artista_id):
    artista = Artista.objects.get(id=artista_id)
    artista.quantidade_musicas -= 1
    artista.save()


def add_duracao_playlist(musicas_ids, playlist_id):
    musicas = Musica.objects.filter(pk__in=musicas_ids)
    playlist = Playlist.objects.get(id=playlist_id)
    tempo_total_musicas = 0

    for musica in musicas:
        tempo_total_musicas += musica.duracao

    playlist.duracao += tempo_total_musicas
    playlist.save()


def sub_duracao_playlist(musicas_ids, playlist_id):
    musicas = Musica.objects.filter(pk__in=musicas_ids)
    playlist = Playlist.objects.get(id=playlist_id)
    tempo_total_musicas = 0

    for musica in musicas:
        tempo_total_musicas += musica.duracao

    if playlist.duracao != 0:
        playlist.duracao -= tempo_total_musicas
        playlist.save()


def add_qnt_msc_playlist(musicas_ids, playlist_id):
    musicas = Musica.objects.filter(pk__in=musicas_ids)
    playlist = Playlist.objects.get(id=playlist_id)

    quantidade_add = int(musicas.count())

    playlist.quantidade_musicas += quantidade_add
    playlist.save()


def sub_qnt_msc_playlist(musicas_ids, playlist_id):
    musicas = Musica.objects.filter(pk__in=musicas_ids)
    playlist = Playlist.objects.get(id=playlist_id)

    quantidade_add = int(musicas.count())

    if playlist.quantidade_musicas != 0:
        playlist.quantidade_musicas -= quantidade_add
        playlist.save()
