from django.urls import path
from rest_framework import routers
from . import views

app_name = 'ratings'

router = routers.SimpleRouter()
router.register('public/avg', views.PublicRatingViewSet)
router.register('', views.RatingViewSet)
urlpatterns = router.urls
