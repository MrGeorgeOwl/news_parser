from parsing.parser import NewsParser


def test_news_parser():

    sites = [
        {"url": "https://www.cnbc.com", "name": "CNBC"},
        {"url": "https://www.nbcnews.com", "name": "NBC"},
        {"url": "https://www.cbsnews.com", "name": "CBS"},
    ]

    news = []
    for site in sites:
        parser = NewsParser(site)
        news.append(parser.parse_news())

    news = list(
        filter(
            lambda articles: articles,
            news
        ),
    )

    assert len(news) == 3
