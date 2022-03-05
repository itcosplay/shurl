from django.contrib import admin
from django.urls import path, include

from shurl.views import render_main_page


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', render_main_page, name='main'),

    path('', include('short_link.urls')),
]
