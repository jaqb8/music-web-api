from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from .serializers import AlbumActivitySerializer
from .models import AlbumActivity
from users.models import UserProfile


class AlbumActivityViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    permission_classes = (IsAuthenticated,)
    serializer_class = AlbumActivitySerializer
    queryset = AlbumActivity.objects.all()

    def get_queryset(self):
        return self.queryset.filter(user=UserProfile.objects.get(user=self.request.user))

    def perform_create(self, serializer):
        return serializer.save(user=UserProfile.objects.get(user=self.request.user))
