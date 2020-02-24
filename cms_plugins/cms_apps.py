# vim:fileencoding=utf-8
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


@apphook_pool.register
class NewsApp(CMSApp):
    name = u'Новости'

    def get_urls(self, page=None, language=None, **kwargs):
        return ["cms_plugins.news_url"]