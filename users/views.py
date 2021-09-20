from rest_framework import generics, views, status, mixins
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from .serializers import RegisterUserSerializer, UserProfileSerializer
from .models import UserProfile


class RegisterUserView(generics.CreateAPIView):
    """Create a new user in the database"""
    serializer_class = RegisterUserSerializer


class BlacklistTokenView(views.APIView):
    """Add token to the blacklist after user logout"""

    @staticmethod
    def post(request):
        try:
            refresh_token = request.data['refresh_token']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'msg': 'Token blacklisted.'})
        except TokenError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except KeyError:
            return Response({'error': 'Provide refresh token.'}, status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(generics.RetrieveAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user


class FollowView(views.APIView):

    def put(self, request, **kwargs):
        my_profile = UserProfile.objects.get(user=request.user)
        obj = UserProfile.objects.get(pk=kwargs['pk'])
        if obj != my_profile:
            my_profile.following.add(obj.user)
        return Response(my_profile.following.all())



