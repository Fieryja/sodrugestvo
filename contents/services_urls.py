from views import ServiceDetail, ServiceList
from django.conf.urls import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'^(?P<slug>.*)/$', ServiceDetail.as_view(), name='service_detail'),
    url(r'^$', ServiceList.as_view(), name='services'),
]