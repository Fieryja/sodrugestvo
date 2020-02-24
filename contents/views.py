# vim:fileencoding=utf-8
from django.views.generic import DetailView, ListView
from contents.models import Service


class ServiceList(ListView):
    template_name = 'contents/services.html'
    model = Service
    context_object_name = 'services'

    def get_queryset(self):
        qs = super(ServiceList, self).get_queryset().filter(active=True)
        return qs

    def get_context_data(self, **kwargs):
        ctx = super(ServiceList, self).get_context_data(**kwargs)
        return ctx


class ServiceDetail(DetailView):
    model = Service
    template_name = "contents/service-detail.html"

    def get_queryset(self):
        qs = super(ServiceDetail, self).get_queryset().filter(active=True)
        return qs

    def get_context_data(self, **kwargs):
        ctx = super(ServiceDetail, self).get_context_data(**kwargs)
        ctx['services'] = Service.objects.filter(active=True)
        return ctx
