from rest_framework import serializers


class ArtistSerializer(serializers.Serializer):
    artist_id = serializers.CharField(max_length=255, source='id')
    artist_name = serializers.CharField(max_length=255, source='name')


class ImageSerializer(serializers.Serializer):
    image_height = serializers.IntegerField(source='height')
    image_width = serializers.IntegerField(source='width')
    image_url = serializers.URLField(source='url')


class SearchItemSerializer(serializers.Serializer):
    item_id = serializers.CharField(max_length=255, source='id')
    item_name = serializers.CharField(max_length=255, source='name')
    item_artists = ArtistSerializer(many=True, source='artists')
    item_images = ImageSerializer(many=True, source='images')


class TrackSerializer(serializers.Serializer):
    track_id = serializers.CharField(max_length=255, source='id')
    track_name = serializers.CharField(max_length=255, source='name')
    track_number = serializers.IntegerField()
    track_preview_url = serializers.CharField(max_length=255, required=False, source='preview_url')


class AlbumSerializer(serializers.Serializer):
    album_id = serializers.CharField(max_length=255, source='id')
    album_name = serializers.CharField(max_length=255, source='name')
    album_artists = ArtistSerializer(many=True, source='artists')
    album_images = ImageSerializer(many=True, source='images')
    album_tracks = TrackSerializer(many=True, source='tracks')
    album_release_date = serializers.CharField(max_length=255, source='release_date')
