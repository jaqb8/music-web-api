from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings


class Rating(models.Model):
    """Album rating object"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    album_rate = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    album_id = models.CharField(max_length=255)

    def __str__(self):
        return f'Album ID: {self.album_id}, Rate: {self.album_rate}, User: {self.user.username}'
