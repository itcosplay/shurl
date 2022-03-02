from django.shortcuts import redirect

from rest_framework.response import Response
from rest_framework.decorators import api_view

from short_link.models import Link
from short_link.serializers import LinkSerializer
# from short_link.utils import make_short_link


@api_view(['POST'])
def create_short_link(request):
    request.data['short_link'] = 'here_must_me_short_link'
    serializer = LinkSerializer(data=request.data)
    # domain = request.META['HTTP_HOST']

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data['short_link'])


@api_view(['GET'])
def redirect_by_short_link(request, short_link):
    redirect_link = Link.objects.get(short_link=short_link).link

    return redirect(redirect_link)