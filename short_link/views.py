import validators

from hashids import Hashids

from django.db.models import Q
from django.shortcuts import redirect
from django.http import JsonResponse
from django.conf import settings

from rest_framework.decorators import api_view

from short_link.models import Link
from short_link.serializers import LinkSerializer
from short_link.serializers import CoustomLinkSerializer


@api_view(['POST'])
def create_short_url(request):
    url = request.data['url']
 
    if not validators.url(url):
        return JsonResponse ({
            'short_url': 'URL isn\'t valid ;('
        })

    existing_links = Link.objects.filter(Q(url=url) | Q(short_url=url))

    if len(existing_links) == 1:
        return JsonResponse ({
            'short_url': existing_links[0].short_url
        })

    elif len(existing_links) > 1:
        return JsonResponse ({
            'error': 'More than one same links exist!'
        })

    serializer = LinkSerializer(data=request.data)
    
    if serializer.is_valid():
        link = serializer.save()
        
        hashids = Hashids(min_length=4)
        hashid = hashids.encode(link.pk)

        short_url = f'http://{settings.DOMAIN}/{hashid}'
        link.short_url = short_url

        link.save()

        return JsonResponse ({
            'short_url': short_url
        })

    else:
        return JsonResponse ({
            'error': 'Something wrong with create...'
        })


@api_view(['POST'])
def create_coustom_url(request):
    url = request.data['url']
    coustom_url_id = request.data['coustom_url']

    if not validators.url(url):
        return JsonResponse ({
            'short_url': 'URL isn\'t valid ;('
        })

    existing_links = Link.objects.filter(Q(url=url) | Q(short_url=url))

    if len(existing_links) == 1:
        link = existing_links[0]
        coustom_url = f'http://{settings.DOMAIN}/{coustom_url_id}'
        link.coustom_url = coustom_url
        link.save()

        return JsonResponse ({
            'coustom_url': coustom_url
        })

    elif len(existing_links) > 1:
        return JsonResponse ({
            'error': 'More than one same links exist...'
        })

    serializer = CoustomLinkSerializer(data=request.data)

    if serializer.is_valid():
        link = serializer.save()

        hashids = Hashids(min_length=4)
        hashid = hashids.encode(link.pk)

        short_url = f'http://{settings.DOMAIN}/{hashid}'
        coustom_url = f'http://{settings.DOMAIN}/{coustom_url_id}'
        link.short_url = short_url
        link.coustom_url = coustom_url

        link.save()

        return JsonResponse ({
            'short_url': short_url,
            'coustom_url': coustom_url
        })

    else:
        return JsonResponse ({
            'error': 'Something wrong with create_coustom...'
        })


@api_view(['GET'])
def redirect_by_short_url(request, url_id):
    url = request.build_absolute_uri()

    redirect_urls = Link.objects.filter (
        Q(short_url=url) | Q(coustom_url=url)
    )
    
    if len(redirect_urls) == 1:
        redirect_url = redirect_urls[0].url
        return redirect(redirect_url)
    
    else:
        return JsonResponse ({
            'error': 'Something wrong with redirect...'
        })