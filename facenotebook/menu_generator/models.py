from django.db import models
from django.urls import reverse


class Menu(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    slug = models.CharField(max_length=255)

    objects = models.Manager

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('show_category',
                       kwargs={'category_slug': self.slug})
