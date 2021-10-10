from collections import defaultdict
from rest_framework import viewsets, mixins
from .serializers import BestOfSerializer
from ratings.models import Rating
from rest_framework.response import Response


class BestOfViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """View set for managing Best of objects from rating models"""
    serializer_class = BestOfSerializer
    queryset = Rating.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.queryset
        serializer = self.get_serializer(queryset, many=True)
        rating_dict = create_dict_with_ratings(serializer)
        return Response({'rating': rating_dict})


def create_dict_with_ratings(serializer):
    """Function for convert from serializer data to dictionary containing album id and list of rating """
    rating_dict = defaultdict(list)
    for item in serializer.data:
        rating_dict[item['album_id']].append(item['album_rate'])
    rating_dict = calculate_rating(rating_dict)
    return rating_dict


def calculate_rating(rating_dict):
    """Function for calculate rating from list of rating"""
    for key in rating_dict:
        rating_dict[key] = sum(rating_dict[key]) / len(rating_dict[key])
    return rating_dict
