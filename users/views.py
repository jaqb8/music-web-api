from rest_framework import generics, views, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from .serializers import RegisterUserSerializer


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
