from core.models import musica, artista, playlist
from rest_framework import serializers
from users.models import User


class MusicaSerializer(serializers.ModelSerializer):

    class Meta:
        model = musica.Musica
        fields = '__all__'


class ArtistaSerializer(serializers.ModelSerializer):

    class Meta:
        model = artista.Artista
        fields = '__all__'


class ArtistaCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = artista.Artista
        fields = ['nome']


class PlayListSerializer(serializers.ModelSerializer):

    class Meta:
        model = playlist.Playlist
        fields = '__all__'


class PlayListCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = playlist.Playlist
        fields = ['nome']


class AddMusicaPlayListSerializer(serializers.ModelSerializer):

    class Meta:
        model = playlist.Playlist
        fields = ['musica']

    def create(self, validated_data):
        playlist = self.initial_data['instance']

        for musica in validated_data['musica']:
            playlist.musica.add(musica)

        return playlist


class RemoverMusicaPlayListSerializer(serializers.ModelSerializer):

    class Meta:
        model = playlist.Playlist
        fields = ['musica']

    def create(self, validated_data):
        playlist = self.initial_data['instance']

        for musica in validated_data['musica']:
            playlist.musica.remove(musica)

        return playlist


class AddUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = '__all__'

    def validate(self, attrs):

        if User.objects.filter(username=attrs['username']).exists():
            print("to aqui porra")
            raise serializers.ValidationError(
                {"username": "username existente"})

        return attrs

    def create(self, validated_data, instance=None):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
