from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = 'users'

urlpatterns = [
    path('register/', views.RegisterUserView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('logout/', views.BlacklistTokenView.as_view(), name='blacklist-token'),
    path('me/', views.UserProfileView.as_view(), name='followers-view'),
    path('follow/<pk>/', views.FollowView.as_view(), name='follow-view')
]
