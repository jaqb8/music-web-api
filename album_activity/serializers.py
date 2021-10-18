from rest_framework import serializers, validators
from .models import AlbumActivity


class AlbumActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumActivity
        fields = ('id', 'album_id', 'activity')
