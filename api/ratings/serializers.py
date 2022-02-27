from rest_framework import serializers
from .models import Rating


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'album_rate', 'album_id', 'comment', 'created_at', 'updated_at')


class UpdateRatingSerializer(RatingSerializer):
    class Meta(RatingSerializer.Meta):
        read_only_fields = ('album_id',)


class BestOfSerializer(serializers.ModelSerializer):
    avg_rate = serializers.DecimalField(max_digits=5, decimal_places=1)

    class Meta:
        model = Rating
        fields = ['album_id', 'avg_rate']