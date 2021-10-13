from rest_framework import serializers, validators
from .models import AlbumActivity


class AlbumActivitySerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = AlbumActivity
        fields = ('id', 'user', 'album_id', 'activity')
        # read_only_fields = ('user',)
        validators = [
            validators.UniqueTogetherValidator(
                queryset=AlbumActivity.objects.all(),
                fields=['user', 'album_id']
            )
        ]
