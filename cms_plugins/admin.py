# vim:fileencoding=utf-8
from codemirror2.widgets import CodeMirrorEditor
from cms.models import Page
from django import forms
from models import Robot, Block, Keyword, ImageBlock
from django.contrib import admin


class ImageBlockAdmin(admin.TabularInline):
    model = ImageBlock


class BlockForm(forms.ModelForm):
    class Meta():
        model = Block
        exclude = []

    html = forms.CharField(widget=CodeMirrorEditor(options={'mode': 'xml', 'theme': 'xq-dark'}))


class BlockAdmin(admin.ModelAdmin):
    list_display = ['name', 'render_tag_name']
    form = BlockForm
    inlines = [ImageBlockAdmin]

    def render_tag_name(self, obj):
        return '{$ block-%s $}' % obj.id

    render_tag_name.allow_tags = True
    render_tag_name.short_description = u'Тэг для вставки'


class FormPage(forms.ModelForm):
    class Meta():
        model = Keyword
        exclude = []
    page = forms.ModelChoiceField(queryset=Page.objects.filter(publisher_is_draft=False), label=u'Страница')


class KeywordAdmin(admin.ModelAdmin):
    form = FormPage


admin.site.register(Block, BlockAdmin)
admin.site.register(Keyword, KeywordAdmin)
admin.site.register(Robot)
