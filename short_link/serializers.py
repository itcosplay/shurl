from rest_framework import serializers

from short_link.models import Link

class LinkDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Link
        fields = ['link']