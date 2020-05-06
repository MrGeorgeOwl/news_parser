from django.db import models

from news_api.models import Article


class NewsSite(models.Model):
    """Model for site where to parse."""
    url = models.CharField(max_length=200)
    name = models.CharField(max_length=50)
