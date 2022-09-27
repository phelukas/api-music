from rest_framework import status, viewsets
from core.serializers import ArtistaSerializer, ArtistaCreateSerializer
from core.models.artista import Artista
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class ArtistaViewSet(viewsets.ViewSet):

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return ArtistaCreateSerializer
        else:
            return ArtistaSerializer

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        return serializer_class(*args, **kwargs)

    def get_queryset(self):
        queryset = Artista.objects.all()
        return queryset

    def get_object(self):
        queryset = self.get_queryset()
        pk = self.kwargs.get('pk')
        obj = get_object_or_404(queryset, pk=pk)
        return obj

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def list(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        artista = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(artista)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        artista = self.get_object()
        artista.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
