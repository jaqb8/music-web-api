from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import UserProfile


class AlbumActivity(models.Model):
    """
    User activity regarding music album.
    For example an album which user is willing to listen in the future can be marked.
    """

    class ActivityEnum(models.TextChoices):
        WANT_TO_LISTEN = 'WTL', _('want to listen')

    user = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE
    )
    album_id = models.CharField(max_length=255)
    activity = models.CharField(
        max_length=3,
        choices=ActivityEnum.choices
    )

    def __str__(self):
        return f'{str(self.user).capitalize()} {self.get_activity_display()} {self.album_id.upper()}'
