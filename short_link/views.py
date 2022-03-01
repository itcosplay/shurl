from rest_framework import generics
from short_link.serializers import LinkDetailSerializer


class CreateShortLinkView(generics.CreateAPIView):
    
    serializer_class = LinkDetailSerializer