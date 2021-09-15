from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import Rating


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'album_rate', 'album_id', 'comment', 'created_at', 'updated_at')


class UpdateRatingSerializer(RatingSerializer):
    class Meta(RatingSerializer.Meta):
        read_only_fields = ('album_id',)
