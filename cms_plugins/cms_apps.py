# vim:fileencoding=utf-8
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


class TariffApp(CMSApp):
    name = u'Тарифы'
    urls = ["contents.tariff_urls"]


apphook_pool.register(TariffApp)


class ServiceApp(CMSApp):
    name = u'Услуги'
    urls = ["contents.services_urls"]


apphook_pool.register(ServiceApp)


class ReviewApp(CMSApp):
    name = u'Отзывы'
    urls = ["contents.reviews_urls"]


apphook_pool.register(ReviewApp)

#
# class MaterialApp(CMSApp):
#     name = u'Материалы'
#     urls = ["contents.material_urls"]
#
#
# apphook_pool.register(MaterialApp)


