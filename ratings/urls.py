from django.urls import path
from . import views

app_name = 'ratings'

urlpatterns = [
    path('create-rating/', views.CreateRatingView.as_view(), name='create-rating')
]
