from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/ratings/', include('ratings.urls')),
    path('api/spotify/', include('spotify_api.urls'))
]
