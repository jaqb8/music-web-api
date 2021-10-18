from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'album_id', 'content', 'created_at', 'updated_at', 'user')


class ReviewCommentSerializer(ReviewSerializer):
    class Meta(ReviewSerializer.Meta):
        read_only_fields = ('album_id',)
