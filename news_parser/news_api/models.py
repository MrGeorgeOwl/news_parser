from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=300, default=None)
    author = models.CharField(max_length=50, default=None)
    url = models.CharField(max_length=500, default=None)
    image_link = models.CharField(max_length=500, default=None)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
