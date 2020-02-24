# vim:fileencoding=utf-8
from cms.models import CMSPlugin, Page
from django.contrib.sites.models import Site
from django.template import Template, Context
from django.template.defaultfilters import safe
from django.db import models
from contents.models import Service, Blog
from sodrugestvo.utils import get_file_path
from sorl.thumbnail import ImageField


class Block(models.Model):
    class Meta():
        verbose_name = u'Блок'
        verbose_name_plural = u'Блоки'

    name = models.CharField(verbose_name=u'Название', max_length=255)
    html = models.TextField(verbose_name=u'Код')

    def __unicode__(self):
        return self.name

    def render(self):
        html = self.html
        if self.images.count():
            ctx = {'img_%s' % i.id: i.image.url for i in self.images.all()}
            html = Template(self.html).render(Context(ctx))
        return html


class ImageBlock(models.Model):
    class Meta():
        verbose_name = u'Изображение'
        verbose_name_plural = u'Изображения и файлы'

    block = models.ForeignKey(Block, related_name='images')
    image = models.FileField(verbose_name=u'Файл', upload_to=get_file_path, blank=True, null=True)

    def __unicode__(self):
        return '{{ img_%s }}' % self.id


class Robot(models.Model):
    class Meta():
        ordering = ['sort']

    name = models.CharField(verbose_name=u'Наименование', max_length=255)
    content = models.TextField(verbose_name=u'Содержимое', max_length=255)
    sort = models.IntegerField(verbose_name=u'Приоритет', default=0)

    def __unicode__(self):
        return self.name


H_CHOICE = (
    ('1', 'H1'),
    ('2', 'H2'),
    ('3', 'H3'),
    ('4', 'H4'),
    ('5', 'H5'),
    ('6', 'H6'),
)


class BaseModelPl(CMSPlugin):
    name = models.CharField(verbose_name=u'Заголовок', blank=True, null=True, max_length=255)
    style = models.CharField(verbose_name=u'Класс блока', max_length=255, blank=True, null=True)
    anchor = models.CharField(verbose_name=u'Якорь', max_length=255, blank=True, null=True)

    def __unicode__(self):
        if self.name:
            return safe(self.name)
        else:
            return u'Блок %s' % self.id


class TextModel(BaseModelPl):
    class Meta():
        verbose_name = u'Текст'

    h = models.CharField(verbose_name=u'Тип заголовка', max_length=255, choices=H_CHOICE, blank=True, null=True)

    def __unicode__(self):
        if self.name:
            return safe(self.name)
        else:
            return u'Текст %s' % self.id


class HtmlInsertModel(CMSPlugin):
    class Meta():
        verbose_name = u'HTML-вставка'
    name = models.CharField(verbose_name=u'Название', max_length=255, blank=True, null=True)
    html = models.TextField(verbose_name=u'Код')
    image = ImageField(verbose_name=u'Изображение', upload_to=get_file_path, blank=True, null=True)

    def __unicode__(self):
        if self.name:
            return self.name


class BlockModel(CMSPlugin):
    class Meta():
        verbose_name = u'HTML-блок'
    block = models.ForeignKey(Block, related_name='plugins', verbose_name=u'Блок')

    def __unicode__(self):
        return self.block.name


class Keyword(models.Model):
    page = models.ForeignKey(Page, related_name='keywords', verbose_name=u'Страница')
    text = models.TextField(verbose_name=u'Keywords')

    def __unicode__(self):
        return self.page.get_title()


class ServicePluginModel(BaseModelPl):
    class Meta():
        verbose_name = u'Услуги'

    services = models.ManyToManyField(Service, verbose_name=u'Тизеры', blank=True)

    def copy_relations(self, oldinstance):
        self.services = oldinstance.services.all()
