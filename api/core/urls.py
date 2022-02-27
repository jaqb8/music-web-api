from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/ratings/', include('ratings.urls')),
    path('api/review/', include('review.urls')),
    path('api/spotify/', include('spotify_api.urls')),
    path('api/album-activity/', include('album_activity.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
