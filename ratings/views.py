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

    def create(self, request, *args, **kwargs):
        """
        Check if album is already rated by currently authenticated user.
        If not create new Rating object.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if len(self.get_queryset().filter(album_id=self.request.data['album_id'])) == 0:
            serializer.save(user=self.request.user)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response({'msg': 'Album has been already rated.'}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        """Delete rating object and return appropriate message"""
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'msg': 'Rating deleted.'}, status=status.HTTP_204_NO_CONTENT)
