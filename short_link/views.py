from django.shortcuts import redirect

from rest_framework.response import Response
from rest_framework.decorators import api_view

from short_link.models import Link
from short_link.serializers import LinkSerializer
from short_link.utils import make_short_url


@api_view(['POST'])
def create_short_url(request):
    request.data['short_url'] = make_short_url(request.data['url'])
    serializer = LinkSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data['short_url'])


@api_view(['GET'])
def redirect_by_short_url(request, short_url):
    redirect_url = Link.objects.get(short_url=short_url).link

    return redirect(redirect_url)