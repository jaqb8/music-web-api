from rest_framework import routers
from . import views

app_name = 'album_activity'

router = routers.SimpleRouter()
router.register('', views.AlbumActivityViewSet)

urlpatterns = router.urls
