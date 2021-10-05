from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .serializers import ReviewSerializer, ReviewCommentSerializer
from .models import Review


class ReviewViewSet(viewsets.ModelViewSet):
    """View set for managing Rating objects in database"""
    permission_classes = (IsAuthenticated,)
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()

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
            return ReviewCommentSerializer
        return self.serializer_class

    def create(self, request, *args, **kwargs):
        """
        Check if album is already rated by currently authenticated user.
        If not create new Rating object.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        """Delete rating object and return appropriate message"""
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'msg': 'Rating deleted.'}, status=status.HTTP_204_NO_CONTENT)


class PublicReviewViewSet(viewsets.ReadOnlyModelViewSet):
    """View set for managing Rating objects in database"""
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()

    def get_queryset(self):
        """
        Return all user's objects and filter by album_id
        """
        album_id = self.request.query_params.get('album_id')
        queryset = self.queryset.filter(album_id=album_id)
        return queryset

    def retrieve(self, request, *args, **kwargs):
        return Response({'msg': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
