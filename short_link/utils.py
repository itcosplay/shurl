from django.conf import settings

from short_link.models import Link


def make_short_url(url):
    if Link.objects.filter(url=url).exists():
        
        return Link.objects.get(url=url).short_url

    links = Link(url=url)
    links.save()

    # hashids = settings(min_length=4)
    hashid = settings.HASHIDS.encode(links.pk)

    short_url = f'{settings.DOMAIN}/{hashid}'
    links.short_url = short_url
    links.save()

    return short_url