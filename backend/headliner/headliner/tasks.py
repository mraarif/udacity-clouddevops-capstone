import json
import os

import requests
from celery import shared_task
from celery.utils.log import get_task_logger

from api.news.models import Article, Source  # pylint: disable=import-error

logger = get_task_logger(__name__)

API_BASE_URL = "https://newsapi.org/v2/top-headlines?country=us"
API_KEY = os.environ.get("NEWS_API_KEY", "")


def save_article(articles):
    for article in articles:
        try:
            logger.info(article)
            source = Source(name=article.get("source").get("name"))
            source.save()
            Article.objects.get_or_create(
                source=source,
                author=article.get("author", ""),
                title=article.get("title", ""),
                url=article.get("url", ""),
                url_to_image=article.get("urlToImage", ""),
                published_at=article.get("publishedAt", ""),
                content=article.get("content", ""),
            )
        except Exception as ex:
            logger.info(ex)
            continue


@shared_task
def seed_articles():
    try:
        response = requests.get(API_BASE_URL, headers={"x-api-key": API_KEY})
        if not response.ok:
            logger.info(response)
            return

        response_json = json.loads(response.content)
        articles = response_json.get("articles")
        save_article(articles)
    except Exception as ex:
        logger.info(ex)
        logger.error(ex)
