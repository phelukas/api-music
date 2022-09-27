from rest_framework import status, viewsets
from core.serializers import MusicaSerializer
from core.models.musica import Musica
from rest_framework.response import Response
from core.utils.helps import add_musica_artista, sub_musica_artista


class MusicaViewSet(viewsets.ModelViewSet):

    queryset = Musica.objects.all()
    serializer_class = MusicaSerializer

    def create(self, request):
        serializer = MusicaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            add_musica_artista(request.data['artista'])
            response = serializer.data
            status_code = status.HTTP_201_CREATED

        else:
            response = serializer.errors
            status_code = status.HTTP_406_NOT_ACCEPTABLE

        return Response(response, status=status_code)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        serializer = MusicaSerializer(
            instance, data=request.data, partial=partial)

        serializer.is_valid(raise_exception=True)

        try:
            if request.data['artista'] != instance.artista.id:
                add_musica_artista(request.data['artista'])
                sub_musica_artista(instance.artista.id)

        except Exception as e:
            if type(e) == KeyError:
                pass
            else:
                raise Exception(e)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)
