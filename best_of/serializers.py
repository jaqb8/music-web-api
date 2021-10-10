from rest_framework import serializers
from ratings.models import Rating


class BestOfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['album_id', 'album_rate']
