import calendar
from datetime import datetime
from django.shortcuts import render_to_response
from django.views.generic import DetailView, ListView
from .models import News, Robot


class NewsList(ListView):
    model = News
    page_template = 'contents/news-endless.html'
    template_name = 'contents/blog.html'

    def get_queryset(self):
        qs = super(NewsList, self).get_queryset().filter(active=True)
        return qs


class NewsDetail(DetailView):
    model = News
    template_name = 'contents/blog-detail.html'

    def get_queryset(self):
        qs = super(NewsDetail, self).get_queryset().filter(active=True)
        return qs


def robots(request):
    ctx = {'robots': Robot.objects.all()}
    return render_to_response('contents/robots.txt', ctx, content_type="text/plain")
