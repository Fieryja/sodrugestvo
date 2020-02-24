# vim:fileencoding=utf-8
from cms.extensions import PageExtension
from cms.models import CMSPlugin
from django.db import models
from filer.fields.image import FilerImageField


class SliderPluginModel(CMSPlugin):
    name = models.CharField(max_length=255, verbose_name=u'Заголовок')
    text = models.CharField(verbose_name=u'Текст', blank=True, null=True, max_length=255)
    html = models.TextField(verbose_name=u'html', blank=True, null=True)
    image = FilerImageField(related_name='sliders', verbose_name=u'Изображение', on_delete=models.PROTECT)
    inner = models.BooleanField(default=False, verbose_name=u'Внутренняя страница')

    def copy_relations(self, oldinstance):
        for associated_item in oldinstance.items.all():
            associated_item.pk = None
            associated_item.plugin = self
            associated_item.save()
