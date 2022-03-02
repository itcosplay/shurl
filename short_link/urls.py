from django.urls import path
from short_link.views import create_short_link
from short_link.views import redirect_by_short_link

urlpatterns = [
    path('create', create_short_link)
]