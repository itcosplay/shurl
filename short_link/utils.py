from tabnanny import check
import validators
from hashids import Hashids

from django.conf import settings

from short_link.models import Link


def is_exists_or_invalid_url(url):
    if Link.objects.filter(url=url).exists():
        return Link.objects.get(url=url).short_url

    if Link.objects.filter(short_url=url).exists():
        return url

    if not validators.url(url):
        return 'URL isn\'t valid ;('


def make_short_url(url):
    checked_url = is_exists_or_invalid_url(url)

    if checked_url:
        return checked_url

    links = Link(url=url)
    links.save()

    hashids = Hashids(min_length=4)
    hashid = hashids.encode(links.pk)

    short_url = f'{settings.DOMAIN}/{hashid}'
    links.short_url = short_url
    links.save()

    return short_url


def make_coustom_url(url, coustom):
    checked_url = is_exists_or_invalid_url(url)

    if checked_url:
        return checked_url

    links = Link(url=url)
    links.save()

    coustom_url = f'{settings.DOMAIN}/{coustom}'
    links.short_url = coustom_url
    links.save()

    return coustom_url


