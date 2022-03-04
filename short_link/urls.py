from django.urls import path
from short_link.views import create_short_url
from short_link.views import get_url_by_short_url


urlpatterns = [
    path('create', create_short_url, name='create_short_url'),
    path('get/<str:short_url>', get_url_by_short_url)
]