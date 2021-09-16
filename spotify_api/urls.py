from django.urls import path
from . import views

app_name = 'spotify_api'

urlpatterns = [
    path('search/', views.SpotifySearchView.as_view(), name='spotify-search'),
    path('album/<str:album_id>', views.SpotifyAlbumView.as_view(), name='spotify-album')
]
