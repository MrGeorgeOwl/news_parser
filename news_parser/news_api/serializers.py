from rest_framework import serializers
from news_api.models import Article


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'author', 'url', 'image_link', 'created_at')
