from rest_framework import viewsets, permissions
from .models import Song, Playlist
from .serializers import SongSerializer, PlaylistSerializer

# Check this name carefully!
class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [permissions.AllowAny]

# Check this name carefully!
class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all() # Added this line to be safe
    serializer_class = PlaylistSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Playlist.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)