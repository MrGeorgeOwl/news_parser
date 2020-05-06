import datetime
import re
from typing import List, Optional

import pydantic
import requests
from bs4 import BeautifulSoup
from opengraph import OpenGraph


class Article(pydantic.BaseModel):
    """Pydantic model for parsed articles."""
    title: str
    author: str
    url: str
    image: Optional[str]
    created_at: datetime.datetime


class NewsParser:
    """Parser for news from net."""

    def __init__(self, site: dict):
        self._url = site["url"]
        self._author = site["name"]

    def parse_news(self) -> List[Article]:
        articles = []
        sitemap_urls = RobotParser(self._url).get_sitemap_urls()
        for sitemap_url in sitemap_urls:
            articles_on_site = self._get_articles(sitemap_url)
            if articles_on_site:
                articles.extend(articles_on_site)
        return articles

    def _get_articles(self, sitemap_url: str) -> List[Article]:
        articles = []
        sitemap = requests.get(sitemap_url).content
        soup = BeautifulSoup(sitemap, 'xml')
        links = soup.find_all('url')
        if not links:
            links = soup.find_all('sitemap')
        for link in links[:10]:
            if link.loc.text.endswith(".xml") or "sitemap" in link.loc.text:
                return self._get_articles(link.loc.text)
            article_dict = self._get_article(link)
            articles.append(Article(**article_dict))
        return articles

    def _get_article(self, url) -> dict:
        url_graph = OpenGraph(url=url.loc.text)
        title = url_graph.title
        created_at = datetime.datetime.now()
        article_dict = {
            "url": url_graph.url,
            "title": title,
            "created_at": created_at,
            "image": url_graph.image,
            "author": self._author,
        }
        return article_dict


class RobotParser:
    """Parser for robots.txt."""
    def __init__(self, url: str):
        if not url.endswith("robots.txt"):
            url += "/robots.txt"
        self._url = url

    def get_sitemap_urls(self) -> List[str]:
        robots = self._get_robots()
        sitemaps = re.findall(r'Sitemap: (.*)', robots)
        return sitemaps

    def _get_robots(self) -> str:
        """Get robots.txt"""
        return requests.get(self._url).text
