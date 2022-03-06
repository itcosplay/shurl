from pyexpat import model
from rest_framework import serializers

from short_link.models import Link


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ['url']


class CoustomLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ['url', 'coustom_url']