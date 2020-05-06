from typing import List
from parsing.parser import Article
from parsing.models import NewsSite
from news_api.models import Article as ArticleDB
from parsing.parser import NewsParser


class ArticleWriter:
    """Class that write parsed articles in database."""
    def __init__(self):
        self._parsed_objects: List[List[Article]] = []

    def write_parsed_objects(self):
        self.parse_objects()
        for parsed_articles in self._parsed_objects:
            self.write(parsed_articles)

    def parse_objects(self) -> None:
        sites = NewsSite.objects.all()
        for site in sites:
            self._parsed_objects.append(NewsParser(site.__dict__).parse_news())

    def write(self, parsed_articles: List[Article]):
        for_create_article = []
        titles = ArticleDB.objects.values_list("title", flat=True)
        for article in parsed_articles:
            if article.title in titles:
                continue
            for_create_article.append(
                ArticleDB(
                    title=article.title,
                    author=article.author,
                    url=article.url,
                    image_link=article.image,
                    created_at=article.created_at,
                )
            )
        ArticleDB.objects.bulk_create(for_create_article)
