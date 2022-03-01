from django.urls import path
from short_link.views import CreateShortLinkView

urlpatterns = [
    path('create', CreateShortLinkView.as_view())
]