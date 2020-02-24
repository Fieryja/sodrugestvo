from django.conf.urls import *

from contents.views import NewsList, NewsDetail

urlpatterns = [
    url(r'^(?P<slug>.*)/$', NewsDetail.as_view(), name='news_detail'),
    url(r'^$', NewsList.as_view(), name='news'),
]
