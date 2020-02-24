# vim:fileencoding=utf-8
from ckeditor.fields import RichTextField
from django.db import models
from django.db.models import permalink
from filer.fields.image import FilerImageField


class Robot(models.Model):
    class Meta():
        ordering = ['sort']

    name = models.CharField(verbose_name=u'Наименование', max_length=255)
    content = models.TextField(verbose_name=u'Содержимое', max_length=255)
    sort = models.IntegerField(verbose_name=u'Приоритет', default=0)

    def __unicode__(self):
        return self.name


class Block(models.Model):
    class Meta():
        verbose_name = u'Блок'
        verbose_name_plural = u'Блоки'

    name = models.CharField(verbose_name=u'Название', max_length=255, help_text=u'Только на латинице')
    comment = models.CharField(verbose_name=u'Описание блока', max_length=255, blank=True, null=True)
    html = models.TextField(verbose_name=u'Код', blank=True, null=True)

    def __str__(self):
        return self.name


class FeedBack(models.Model):
    class Meta():
        verbose_name = u'Обратная связь'
        verbose_name_plural = u'Обратная связь'

    name = models.CharField(verbose_name=u'Имя', max_length=255, blank=True, null=True)
    phone = models.CharField(verbose_name=u'Телефон', max_length=255, blank=True, null=True)
    email = models.CharField(verbose_name=u'Email', max_length=255, blank=True, null=True)
    text = models.TextField(verbose_name=u'Сообщение', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, verbose_name=u'Дата')

    def __str__(self):
        return self.name


class News(models.Model):
    class Meta():
        verbose_name_plural = u'Новости'
        verbose_name = u'Новость'
        ordering = ['-date']

    name = models.CharField(max_length=255, verbose_name=u'Название')
    image = FilerImageField(related_name='news', verbose_name=u'Изображение', blank=True, null=True,
                            on_delete=models.PROTECT)
    slug = models.SlugField(max_length=255, unique=True, verbose_name=u'URL')
    text = RichTextField(verbose_name=u'Описание', blank=True, null=True, )
    date = models.DateTimeField(verbose_name=u'Дата')
    date_added = models.DateTimeField(verbose_name=u'Дата добавления', auto_now_add=True)
    active = models.BooleanField(verbose_name=u'Активность', default=True)
    meta_title = models.CharField(max_length=255, verbose_name=u'Тайтл', null=True, blank=True)
    meta_keywords = models.TextField(verbose_name=u'Keywords', null=True, blank=True)
    meta_description = models.TextField(max_length=255, verbose_name=u'Description', null=True, blank=True)

    def __str__(self):
        return self.name

    @permalink
    def get_absolute_url(self):
        return 'news_detail', (self.slug, ), {}
