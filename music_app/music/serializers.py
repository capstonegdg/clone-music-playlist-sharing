from rest_framework import serializers
from .models import Song, Playlist
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'artist', 'audio_file', 'cover_image']

class PlaylistSerializer(serializers.ModelSerializer):
    # This shows the actual song details inside the playlist
    songs = SongSerializer(many=True, read_only=True)
    # This allows us to add songs by their ID when creating/editing
    song_ids = serializers.PrimaryKeyRelatedField(
        many=True, write_only=True, queryset=Song.objects.all(), source='songs'
    )

    class Meta:
        model = Playlist
        fields = ['id', 'user', 'name', 'songs', 'song_ids']