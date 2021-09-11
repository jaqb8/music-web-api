from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import Rating


class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = ('album_rate', 'album_id')
        validators = [
            UniqueTogetherValidator(
                queryset=Rating.objects.all(),
                fields=['album_id'],
                message='Album has already been rated.'
            )
        ]

    # def create(self, validated_data):
    #     print(validated_data)
    #     return Rating.objects.create(**validated_data)