from django.contrib import admin

from short_link.models import Link


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ['url', 'short_url']
