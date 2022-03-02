from django.core.management.base import BaseCommand
from django.conf import settings

class Command(BaseCommand):
    help = 'Creates short url(s) from url(urls)'

    def add_arguments(self, parser):
        parser.add_argument('urls', nargs='+', type=str)

    def handle(self, urls, *args, **kwargs):
        for url in urls:
            make_short_link(url)


def make_short_link(url):
    # https://www.google.ru/
    # print(settings.DOMAIN)
    pass