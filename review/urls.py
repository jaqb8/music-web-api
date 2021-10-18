from django.urls import path
from rest_framework import routers
from . import views

app_name = 'review'

router = routers.SimpleRouter()
router.register('public', views.PublicReviewViewSet)
router.register('', views.ReviewViewSet)

urlpatterns = router.urls
