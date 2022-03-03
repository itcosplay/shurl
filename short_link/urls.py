from django.urls import path
from short_link.views import create_short_url


urlpatterns = [
    path('create', create_short_url)
]