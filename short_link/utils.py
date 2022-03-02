from django.contrib.sites.models import Site


def make_short_link():
    current_site = Site.objects.get_current()
    
    return current_site.domain