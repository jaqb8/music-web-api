from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import Rating


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'album_rate', 'album_id', 'comment')
        validators = [
            UniqueTogetherValidator(
                queryset=Rating.objects.all(),
                fields=['album_id'],
                message='Album has already been rated.'
            )
        ]


class UpdateRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'album_rate', 'album_id', 'comment')
        read_only_fields = ('album_id',)
