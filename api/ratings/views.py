from rest_framework import status, viewsets, mixins
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import RatingSerializer, UpdateRatingSerializer, BestOfSerializer
from .models import Rating
from users.models import UserProfile
from django.db.models import Avg


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
        queryset = self.queryset.filter(user=self._get_user_profile())
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
            serializer.save(user=self._get_user_profile())
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response({'msg': 'Album has been already rated.'}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        """Delete rating object and return appropriate message"""
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'msg': 'Rating deleted.'}, status=status.HTTP_204_NO_CONTENT)

    def _get_user_profile(self):
        return UserProfile.objects.get(user=self.request.user)


class PublicRatingViewSet(viewsets.ReadOnlyModelViewSet):
    """View set for managing Rating objects in database"""
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()

    def get_queryset(self):
        """
        Return all user's objects and filter by album_id
        """
        album_id = self.request.query_params.get('album_id')
        queryset = self.queryset.filter(album_id=album_id)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        avg = round(queryset.aggregate(Avarage_name=Avg('album_rate'))['Avarage_name'], 1)
        rating_count = queryset.count()
        return Response({'avg': avg, 'count': rating_count})

    def retrieve(self, request, *args, **kwargs):
        return Response({'msg': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)


class BestOfViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """View set for managing Best of objects from rating models"""
    serializer_class = BestOfSerializer
    queryset = Rating.objects.values('album_id').annotate(avg_rate=Avg('album_rate')).order_by('-avg_rate')
