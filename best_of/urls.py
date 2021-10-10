from django.urls import path
from rest_framework import routers
from . import views

app_name = 'bestof'

router = routers.SimpleRouter()
router.register('', views.BestOfViewSet)
urlpatterns = router.urls
