from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import SimpleRouter

app_name = 'users'

router = SimpleRouter()
router.register('', views.UserProfileViewSet)

urlpatterns = [
    path('register/', views.RegisterUserView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('logout/', views.BlacklistTokenView.as_view(), name='blacklist-token'),
    path('profile/', include(router.urls))
]
