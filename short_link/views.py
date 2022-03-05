from django.shortcuts import redirect
from django.http import JsonResponse
from django.conf import settings

from rest_framework.decorators import api_view

from short_link.models import Link
from short_link.serializers import LinkSerializer
from short_link.utils import make_short_url


@api_view(['POST'])
def create_short_url(request):
    short_url = make_short_url(request.data['url'])
    serializer = LinkSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save(short_url=short_url, coustom_url='')
    
    return JsonResponse({
        'short_url': short_url
    })


@api_view(['GET'])
def redirect_by_short_url(request, short_id):
    short_url = f'{settings.DOMAIN}/{short_id}'
    redirect_url = Link.objects.get(short_url=short_url).url

    return redirect(redirect_url)