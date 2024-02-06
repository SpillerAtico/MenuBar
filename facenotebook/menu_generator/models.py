from django.db import models
from django.urls import reverse


class Users(models.Model):
    name = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    is_friend = models.BooleanField(default=True)
    slug = models.SlugField(max_length=255, blank=True, db_index=True, default='')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('friend', kwargs={'friend_slug': self.slug})
