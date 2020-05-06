from django.db import models
from django.utils.timezone import now


class Article(models.Model):
    title = models.CharField(max_length=300, default=None)
    author = models.CharField(max_length=50, default=None)
    url = models.CharField(max_length=500, default=None)
    image_link = models.CharField(max_length=500, default=None)
    created_at = models.DateField(default=now)

    def __str__(self):
        return self.title
