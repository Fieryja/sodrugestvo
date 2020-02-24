from django.conf.urls import *
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt

from .ajax_views import *

admin.autodiscover()


urlpatterns = [
    url(r'^feedback/$', csrf_exempt(feed_back), name='feed_back'),
]
