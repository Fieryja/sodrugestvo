from uuid import uuid4

from django import forms
from django.contrib.sites.shortcuts import get_current_site
from django.core.files.base import ContentFile
from django.core.mail import EmailMessage
from django.template import loader

from contents.models import FeedBack
from django.conf import settings


class FeedBackForm(forms.ModelForm):
    class Meta():
        model = FeedBack
        exclude = []


def feed_back(request):
    data = request.POST.copy()
    form = FeedBackForm(data)
    if form.is_valid():
        back = form.save()
        context = {'form': back, 'site': get_current_site(request), 'static': settings.STATIC_URL}
        temp = loader.get_template("mail/feedback.html")
        html = (temp.render(context)).encode('utf-8')
        to_email = [data.get('to_email', False)] if data.get('to_email', False) else settings.DEFAULT_TO_EMAIL
        msg = EmailMessage(u'Новое сообщение', html, settings.DEFAULT_FROM_EMAIL, to_email, headers={})
        msg.content_subtype = "html"
        msg.send()
        return {'success': True, 'form': True}
    return {}
