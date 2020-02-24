# vim:fileencoding=utf-8
from cms.models import admin
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from codemirror2.widgets import CodeMirrorEditor
from django import forms
from django.template import Template, Context
from models import HtmlInsertModel, BlockModel, TextModel, BaseModelPl, ServicePluginModel


class HtmlForm(forms.ModelForm):
    class Meta():
        model = HtmlInsertModel
        exclude = []

    html = forms.CharField(widget=CodeMirrorEditor(options={'mode': 'xml', 'theme': 'xq-dark'}))


class HtmlInsertPlugin(CMSPluginBase):
    model = HtmlInsertModel
    name = u'Html вставка'
    form = HtmlForm
    render_template = 'plugins/html-insert.html'

    def render(self, context, instance, placeholder):
        html = instance.html
        if instance.image:
            html = Template(instance.html).render(Context({'img': instance.image.url}))
        context.update({'plugin': instance, 'html': html})
        return context


class BlockInsertPlugin(CMSPluginBase):
    model = BlockModel
    name = u'Блок'
    render_template = 'plugins/html-insert.html'

    def render(self, context, instance, placeholder):
        context.update({'plugin': instance})
        return context


class TextPlugin(CMSPluginBase):
    model = TextModel
    render_template = 'plugins/text.html'
    name = u'Текст'

    def render(self, context, instance, placeholder):
        context.update({'plugin': instance})
        return context


class ServicePlugin(CMSPluginBase):
    model = ServicePluginModel
    render_template = 'plugins/services.html'
    filter_horizontal = ['services']
    name = u'Услуги'

    def render(self, context, instance, placeholder):
        context.update({'plugin': instance})
        return context



plugin_pool.register_plugin(ServicePlugin),
plugin_pool.register_plugin(TextPlugin),
plugin_pool.register_plugin(BlockInsertPlugin),
plugin_pool.register_plugin(HtmlInsertPlugin),
