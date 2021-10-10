from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/ratings/', include('ratings.urls')),
    path('api/review/', include('review.urls')),
    path('api/spotify/', include('spotify_api.urls')),
    path('api/bestof/', include('best_of.urls')),
]
