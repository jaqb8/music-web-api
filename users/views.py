from rest_framework import generics
from .serializers import RegisterUserSerializer


class RegisterUserView(generics.CreateAPIView):
    """Create a new user in the database"""
    serializer_class = RegisterUserSerializer
