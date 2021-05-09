from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
from django.db.models import Model


class Source(Model):
    name = models.CharField(_('name'), max_length=200)


class Article(Model):
    source = models.OneToOneField(Source, on_delete=models.CASCADE,
                                  related_name='related_article')
    author = models.CharField(_('author'), max_length=250, null=True)
    title = models.CharField(_('title'), max_length=300)
    url = models.URLField(_('url'), max_length=500, null=True)
    url_to_image = models.URLField(_('image url'), max_length=500, null=True)
    published_at = models.DateTimeField(_("published at"))
    content = models.TextField(_("content"))
