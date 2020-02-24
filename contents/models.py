from django.db import models


TEMPLATE_TYPE = (
    ('page', 'Страница'),
    ('tilda', 'Tilda'),
    ('text', 'Текст'),
    ('image', 'Изображение'),
)


class Template(models.Model):
    class Meta:
        pass

    name = models.CharField(max_length=255)
    html = models.TextField(blank=True, null=True)
    path = models.CharField(max_length=255, blank=True, null=True)
    type_temp = models.CharField(max_length=255, choices=TEMPLATE_TYPE, default='page')
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)


class Page(models.Model):
    class Meta():
        verbose_name_plural = u'Страницы'

    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    publish = models.BooleanField(default=False)
    html = models.TextField(blank=True, null=True)
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_keyword = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    date_publish = models.DateTimeField(blank=True, null=True)


class Slot(models.Model):
    class Meta:
        pass

    page = models.ForeignKey(Page, on_delete=models.CASCADE)


class Plugin(models.Model):
    class Meta:
        pass

    slot = models.ForeignKey(Page, on_delete=models.CASCADE)
    template = models.ForeignKey(Template, on_delete=models.CASCADE)
