# vim:fileencoding=utf-8
from cms.models import PlaceholderField, User
from django.db import models
from django.db.models import permalink
from sorl.thumbnail import ImageField
from sodrugestvo.utils import get_file_path


class FeedBack(models.Model):
    class Meta():
        verbose_name = u'Обратная связь'
        verbose_name_plural = u'Обратная связь'

    name = models.CharField(verbose_name=u'Имя', max_length=255, blank=True, null=True)
    email = models.CharField(verbose_name=u'E-mail', max_length=255, blank=True, null=True)
    phone = models.CharField(verbose_name=u'Телефон', max_length=255, blank=True, null=True)
    comment = models.TextField(verbose_name=u'Коментарий', blank=True, null=True)
    date = models.DateTimeField(verbose_name=u'Дата', auto_now_add=True)

    def __unicode__(self):
        if self.name:
            return self.name
        if self.email:
            return self.email
        if self.phone:
            return self.phone
        return self.date


class Service(models.Model):
    class Meta():
        verbose_name_plural = u'Услуги'
        verbose_name = u'Услуга'
        ordering = ['sort']

    name = models.CharField(verbose_name=u'Название', max_length=255)
    slug = models.SlugField(verbose_name=u'URL', max_length=255, unique=True)
    image = ImageField(verbose_name=u'Изображение', upload_to=get_file_path)
    short = models.TextField(verbose_name=u'Краткое описание')
    text = models.TextField(verbose_name=u'Подробное описание', blank=True, null=True)
    sort = models.IntegerField(default=0, verbose_name=u'Приоритет')
    active = models.BooleanField(verbose_name=u'Активность', default=True)

    def __unicode__(self):
        return self.name

    @permalink
    def get_absolute_url(self):
        return 'service_detail', (self.slug, ), {}


class Blog(models.Model):
    class Meta():
        verbose_name_plural = u'Блог'
        verbose_name = u'Пост'
        ordering = ['-date']

    name = models.CharField(verbose_name=u'Название', max_length=255)
    slug = models.SlugField(verbose_name=u'URL', max_length=255, unique=True)
    image = ImageField(verbose_name=u'Изображение', upload_to=get_file_path)
    short = models.TextField(verbose_name=u'Краткое описание')
    text = models.TextField(verbose_name=u'Подробное описание', blank=True, null=True)
    active = models.BooleanField(verbose_name=u'Активность', default=True)
    date = models.DateTimeField(verbose_name=u'Дата')

    def __unicode__(self):
        return self.name

    @permalink
    def get_absolute_url(self):
        return 'service_detail', (self.slug, ), {}
