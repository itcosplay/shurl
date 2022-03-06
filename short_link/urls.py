from django.urls import path
from short_link.views import create_short_url
from short_link.views import create_coustom_url
from short_link.views import redirect_by_short_url


urlpatterns = [
    path('create', create_short_url, name='create_short_url'),
    path('create_coustom', create_coustom_url, name='create_coustom_url'),
    path('<str:url_id>', redirect_by_short_url)
]