from cms.sitemaps import CMSSitemap
from django.conf.urls import *
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from cms_plugins.views import robots
from sodrugestvo import settings

sitemaps1 = {
    'cmspages': CMSSitemap,
}


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^robots\.txt$', robots),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps1}),
    url(r'', include('cms.urls')),


]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)