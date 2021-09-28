from rest_framework import generics, views, status, viewsets, decorators
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


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UserProfileSerializer

    @decorators.action(methods=['POST'], detail=True, url_path='follow')
    def follow_user(self, request, pk=None):
        """Add user to following list and return response with whole following list"""
        instance = self.get_object()
        authenticated_user = UserProfile.objects.get(user=request.user)
        serializer = self.get_serializer(authenticated_user, data=request.data)
        serializer.is_valid(raise_exception=True)

        if authenticated_user == instance:
            return Response({'msg': 'Unable to follow own profile'},
                            status=status.HTTP_400_BAD_REQUEST)
        else:
            authenticated_user.following.add(instance.user)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
