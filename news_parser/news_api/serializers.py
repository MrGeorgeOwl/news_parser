from rest_framework import serializers
from news_api.models import Article


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ('label', 'author', 'url', 'created_at')
