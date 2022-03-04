from django.shortcuts import redirect
from django.http import JsonResponse
from django.conf import settings

from rest_framework.response import Response
from rest_framework.decorators import api_view

from short_link.models import Link
from short_link.serializers import LinkSerializer
from short_link.utils import make_short_url


@api_view(['POST'])
def create_short_url(request): 
    short_url = make_short_url(request.data['url'])
    serializer = LinkSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save(short_url=short_url)
    
    return JsonResponse({
        'url': serializer.data['url'],
        'short_url': short_url
    })
 

@api_view(['GET'])
def redirect_by_short_url(request, short_url):
    url_pk = settings.HASHIDS.decode(short_url)[0]
    redirect_url = Link.objects.get(pk=url_pk).url

    return redirect(redirect_url)


@api_view(['GET'])
def get_url_by_short_url(request, short_url):
    url = Link.objects.filter(short_url__contains=short_url)[0]
    serializer = LinkSerializer(url)

    return Response(serializer.data)