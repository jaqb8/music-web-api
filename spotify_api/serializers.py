from rest_framework import serializers


class ArtistSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=255)
    name = serializers.CharField(max_length=255)


class ImageSerializer(serializers.Serializer):
    height = serializers.IntegerField()
    width = serializers.IntegerField()
    url = serializers.URLField()


class SearchItemSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=255)
    name = serializers.CharField(max_length=255)
    artists = ArtistSerializer(many=True)
    images = ImageSerializer(many=True)


class TrackSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=255)
    name = serializers.CharField(max_length=255)
    track_number = serializers.IntegerField()
    preview_url = serializers.CharField(max_length=255, required=False)


class AlbumSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=255)
    name = serializers.CharField(max_length=255)
    artists = ArtistSerializer(many=True)
    images = ImageSerializer(many=True)
    tracks = TrackSerializer(many=True)
    release_date = serializers.CharField(max_length=255)
