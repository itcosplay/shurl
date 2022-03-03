from django.core.management.base import BaseCommand

from short_link.utils import make_short_url

class Command(BaseCommand):
    help = 'Creates short url(s) from url(urls)'

    def add_arguments(self, parser):
        parser.add_argument('urls', nargs='+', type=str)

    def handle(self, urls, *args, **kwargs):
        for url in urls:
            show_short_url(url)


def show_short_url(url):
    print (
        url, ' <--> ', make_short_url(url)
    )