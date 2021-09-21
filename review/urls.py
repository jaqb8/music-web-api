from django.urls import path
from rest_framework import routers
from . import views

app_name = 'review'

router = routers.SimpleRouter()
# router.register('', views.ReviewViewSet)
router.register('', views.PublicReviewViewSet)

urlpatterns = router.urls
