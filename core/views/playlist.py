from rest_framework import status, viewsets
from core.serializers import RemoverMusicaPlayListSerializer, AddMusicaPlayListSerializer, PlayListCreateSerializer, PlayListSerializer
from core.models.playlist import Playlist
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from core.utils.helps import sub_qnt_msc_playlist, add_qnt_msc_playlist, add_duracao_playlist, sub_duracao_playlist
from rest_framework.views import APIView


class PlayListViewSet(viewsets.ModelViewSet):

    queryset = Playlist.objects.all()
    serializer_class = PlayListSerializer

    def create(self, request):
        serializer = PlayListCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        data = request.data

        serializer = PlayListCreateSerializer(
            instance, data=request.data, partial=partial)

        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class PlayListAddView(APIView):

    def post(self, request, format=None, pk=None):
        pk = self.kwargs['pk']
        playlist = Playlist.objects.filter(pk=pk)

        if len(playlist) == 0:
            msg = f'Play list com id {pk} não encontrada'
            return Response({"error": msg}, status=status.HTTP_404_NOT_FOUND)

        data = request.data
        data['instance'] = playlist.first()

        serializer = AddMusicaPlayListSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        add_duracao_playlist(data['musica'], pk)
        add_qnt_msc_playlist(data['musica'], pk)

        return Response(serializer.data, status=status.HTTP_200_OK)


class PlayListRemoverView(APIView):

    def post(self, request, format=None, pk=None):
        pk = self.kwargs['pk']
        playlist = Playlist.objects.filter(pk=pk)

        if len(playlist) == 0:
            msg = f'Play list com id {pk} não encontrada'
            return Response({"error": msg}, status=status.HTTP_404_NOT_FOUND)

        data = request.data
        data['instance'] = playlist.first()

        serializer = RemoverMusicaPlayListSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        sub_duracao_playlist(data['musica'], pk)
        sub_qnt_msc_playlist(data['musica'], pk)

        return Response(serializer.data, status=status.HTTP_200_OK)
