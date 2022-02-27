from rest_framework import views, status
from rest_framework.response import Response
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from .api_models import SearchItem, Album
from .serializers import SearchItemSerializer, AlbumSerializer


class SpotifyBaseView(views.APIView):
    """Base Spotify view with Spotify authentication"""
    spotify_client = spotipy.Spotify(auth_manager=SpotifyClientCredentials())


class SpotifySearchView(SpotifyBaseView):
    """Perform Spotify API search"""

    def get(self, request):
        query = request.query_params.get('q', '')
        if query:
            response = self.spotify_client.search(q=query, type='album')
            response = self._filter_search_response(response)
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response({'msg': 'Query parameter not provided.'}, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def _filter_search_response(response):
        search_items = [SearchItem(
            id=item['id'],
            name=item['name'],
            artists=item['artists'],
            images=item['images']
        ) for item in response['albums']['items']]
        serializer = SearchItemSerializer(search_items, many=True)
        return serializer.data


class SpotifyAlbumView(SpotifyBaseView):
    """Get single album from Spotify API by its ID"""

    def get(self, _, album_id):
        try:
            response = self.spotify_client.album(album_id)
            response = self._filter_album_response(response)
        except spotipy.exceptions.SpotifyException as e:
            return Response({'msg': f'Spotify API error: {e.msg}'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(response, status=status.HTTP_200_OK)

    @staticmethod
    def _filter_album_response(response):
        album = Album(
            id=response['id'],
            name=response['name'],
            artists=response['artists'],
            images=response['images'],
            tracks=response['tracks']['items'],
            release_date=response['release_date']
        )
        serializer = AlbumSerializer(album)
        return serializer.data
