from django.db import models


class ShortUrl(models.Model):
    url = models.URLField(verbose_name='Ссылка', null=False, unique=True)
    short_url = models.URLField(verbose_name='Короткая ссылка', unique=True, null=False)
