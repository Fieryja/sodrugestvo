# vim:fileencoding=utf-8
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import SliderPluginModel


@plugin_pool.register_plugin
class SliderPlugin(CMSPluginBase):
    model = SliderPluginModel
    name = u'Слайдер'
    render_template = "plugins/slider.html"

    def render(self, context, instance, placeholder):
        context = super(SliderPlugin, self).render(context, instance, placeholder)
        context.update({
            'plugin': instance,
        })
        return context
