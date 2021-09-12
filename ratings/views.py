from django.shortcuts import render
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import RatingSerializer, UpdateRatingSerializer
from .models import Rating


class RatingViewSet(viewsets.ModelViewSet):
    """View set for managing Rating objects in database"""
    permission_classes = (IsAuthenticated,)
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()

    def get_queryset(self):
        """
        Return only current authenticated user's objects
        and filter by album_id if provided as query parameter
        """
        queryset = self.queryset.filter(user=self.request.user)
        album_id = self.request.query_params.get('album_id')
        if album_id:
            queryset = queryset.filter(album_id=album_id)
        return queryset

    def get_serializer_class(self):
        """Return appropriate serializer class based on called endpoint"""
        if self.action == 'update':
            return UpdateRatingSerializer
        return self.serializer_class

    def perform_create(self, serializer):
        """Create new rating object with current authenticated user's info attached"""
        serializer.save(user=self.request.user)

    def destroy(self, request, *args, **kwargs):
        """Delete rating object and return appropriate message"""
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'msg': 'Rating deleted.'}, status=status.HTTP_204_NO_CONTENT)
