"""zelda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import logout
from django.conf.urls.static import static
from cms.sitemaps import CMSSitemap
from django.conf.urls import url, include
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from django.views.i18n import JavaScriptCatalog

from contents.models import News

news_dict = {
    'queryset': News.objects.filter(active=True),
    'date_field': 'date_added',
}


sitemaps = {
    'news': GenericSitemap(news_dict, priority=0.6),
    'cmspages': CMSSitemap}

from contents.views import robots

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^robots\.txt$', robots),
    url(r'^ajax/', include('contents.ajax_urls')),
    url(r'^filebrowser_filer/', include('ckeditor_filebrowser_filer.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^logout/$', logout, {'next_page': '/'}, name='logout'),
    url(r'^filer/', include('filer.urls')),
    url('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    url(r'^', include('cms.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
