from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import AlbumActivitySerializer
from .models import AlbumActivity
from users.models import UserProfile


class AlbumActivityViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    """View set for managing Album Activity objects in database"""
    permission_classes = (IsAuthenticated,)
    serializer_class = AlbumActivitySerializer
    queryset = AlbumActivity.objects.all()

    def get_queryset(self):
        """Return only objects which were created by current authenticated user"""
        return self.queryset.filter(user=self._get_user_profile())

    def create(self, request, *args, **kwargs):
        """Overridden generic create method to check if user already marked album"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if len(self.get_queryset().filter(album_id=self.request.data['album_id'])) == 0:
            serializer.save(user=self._get_user_profile())
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response({'msg': 'Album already has activity assigned.'}, status=status.HTTP_400_BAD_REQUEST)

    def _get_user_profile(self):
        return UserProfile.objects.get(user=self.request.user)
