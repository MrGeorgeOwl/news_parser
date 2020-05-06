"""Module with tests for RobotParser"""
import pytest

from parsing.parser import RobotParser


sites = ["https://www.cnbc.com", "https://www.nbcnews.com", "https://www.cbsnews.com"]


def test_sites_have_sitemaps():
    sitemaps = []
    for site in sites:
        rb = RobotParser(site)
        sitemaps.append(rb.get_sitemap_urls())
    sitemaps = list(
        filter(
            lambda x: x,
            sitemaps
        )
    )
    print(sitemaps)
    assert len(sitemaps) == 3
