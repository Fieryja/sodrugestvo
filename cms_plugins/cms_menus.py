# vim:fileencoding=utf-8
from django.contrib.sites.shortcuts import get_current_site
from menus.base import NavigationNode
from menus.menu_pool import menu_pool
from cms.menu_bases import CMSAttachMenu

from contents.models import Service, Tariff


class CatalogMenu(CMSAttachMenu):

    name = u'Меню услуг'

    def get_nodes(self, request):
        nodes = []
        l = Service.objects.filter(active=True)
        for p in l:
            nodes.append(NavigationNode(p.name, p.get_absolute_url(), p.id))
        return nodes

menu_pool.register_menu(CatalogMenu)


class TariffMenu(CMSAttachMenu):

    name = u'Меню Тарифов'

    def get_nodes(self, request):
        nodes = []
        l = Tariff.objects.filter(active=True)
        for p in l:
            nodes.append(NavigationNode(p.name, p.get_absolute_url(), p.id))
        return nodes

menu_pool.register_menu(TariffMenu)