from rest_framework import serializers

from short_link.models import Link
from short_link.utils import make_short_url


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        # fields = ['url']
        fields = '__all__'