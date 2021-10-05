from django.db import models
from django.conf import settings


class Review(models.Model):
    """ Album review model"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    album_id = models.CharField(max_length=255)
    content = models.TextField(max_length=350, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Album ID: {self.album_id}, Content: {self.content}, User: {self.user.username}'
