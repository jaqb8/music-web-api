from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from users.models import UserProfile


class Rating(models.Model):
    """Album rating object"""
    class Meta:
        ordering = ('-updated_at',)

    user = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE
    )
    album_rate = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    album_id = models.CharField(max_length=255)
    comment = models.TextField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Album ID: {self.album_id}, Rate: {self.album_rate}, User: {self.user}'
