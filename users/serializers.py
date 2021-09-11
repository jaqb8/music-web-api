from django.contrib.auth import get_user_model
from rest_framework import serializers


class RegisterUserSerializer(serializers.ModelSerializer):
    """Serializer for user registration"""

    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'email')
        extra_kwargs = {
            'password': {
                'write_only': True
            },
            'email': {
                'required': True
            }
        }

    def create(self, validated_data):
        """Create a new user and return it"""
        return get_user_model().objects.create_user(**validated_data)
