# coding=utf-8
import os
import uuid
from datetime import datetime
from sorl.thumbnail.base import ThumbnailBackend
from os.path import basename
from sorl.thumbnail.helpers import tokey, serialize
from django.http import HttpResponseRedirect
from slugify import slugify
from django.conf import settings


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    if getattr(instance, 'name', False):
        filename = "%s.%s" % (slugify(instance.name), ext)
    elif getattr(instance, 'page', False):
        filename = "%s.%s" % (slugify(instance.page.get_title()), ext)
    elif getattr(instance, 'gallery', False):
        filename = "%s.%s" % (slugify(instance.gallery.name), ext)
    else:
        filename = "%s.%s" % (uuid.uuid4(), ext)
    now = datetime.now()
    return os.path.join(getattr(settings, 'IMAGE_UPLOAD_TO', 'catalog/'), datetime.strftime(now, '%Y/%m/'), filename)


class SEOThumbnailBackend(ThumbnailBackend):
    def _get_thumbnail_filename(self, source, geometry_string, options):
        key = tokey(source.key, geometry_string, serialize(options))
        path = '%s/%s/%s' % (key[:2], key[2:4], key)
        return '%s%s/%s' % (settings.THUMBNAIL_PREFIX, path, basename(source.name))


def copy_object(modeladmin, request, queryset):
    for pr in queryset:
        pr.pk = None
        pr.id = None
        try:
            if pr.slug:
                pr.slug = slugify(pr.name)[:46]
                slug_test = ''
                i = 1
                exists = modeladmin.model.objects.filter(slug=pr.slug).exists()
                while exists:
                    slug_test = u'%s-%s' % (pr.slug, i)
                    exists = modeladmin.model.objects.filter(slug=slug_test).exists()
                    i += i
                if slug_test:
                    pr.slug = slug_test
        except:
            pass
        pr.save()
    modeladmin.message_user(request, u'Копирование завершено')
    return HttpResponseRedirect(request.get_full_path())


copy_object.short_description = u'Копирование объекта'
