from django.db import models
from django.contrib.auth import get_user_model


class UserProfile(models.Model):
    """Extension to Django build-in user model for more information"""
    class Meta:
        ordering = ('-created_at',)

    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    following = models.ManyToManyField(get_user_model(), related_name='following', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def profiles_ratings(self):
        """Returns all ratings related to user profile"""
        return self.rating_set.all()

    def __str__(self):
        return str(self.user.username)
