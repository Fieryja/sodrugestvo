# coding=utf-8
import json
import os
import uuid
from datetime import datetime
from django.conf import settings
from django.contrib.sites.models import Site
from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect
from django.template import Context, loader
from slugify import slugify


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    now = datetime.now()
    return os.path.join(getattr(settings, 'IMAGE_UPLOAD_TO', 'content/'), datetime.strftime(now, '%Y/%m/'), filename)


def create_slug(model, name):
    slug = slugify(name)
    slug_test = ''
    i = 1
    exists = model.objects.filter(slug=slug).exists()
    while exists:
        slug_test = u'%s-%s' % (slug, i)
        exists = model.objects.filter(slug=slug_test).exists()
        i += i
    if slug_test:
        slug = slug_test
    return slug


def copy_object(modeladmin, request, queryset):
    for pr in queryset:
        pr.pk = None
        pr.id = None
        try:
            pr.slug = create_slug(modeladmin.model, pr.name)
        except:
            pass
        pr.save()
    modeladmin.message_user(request, u'Копирование завершено')
    return HttpResponseRedirect(request.get_full_path())


copy_object.short_description = u'Копирование объекта'


def send_mail(ctx, template, theme, email=settings.DEFAULT_TO_EMAIL, heads={}):
    site = Site.objects.get(id=1)
    context = {'site': site, 'STATIC_URL': settings.STATIC_URL}
    context.update(ctx)
    temp = loader.get_template(template)
    html = (temp.render(context)).encode('utf-8')
    msg = EmailMessage(theme, html, settings.DEFAULT_FROM_EMAIL, email, heads)
    msg.content_subtype = "html"
    msg.send()
