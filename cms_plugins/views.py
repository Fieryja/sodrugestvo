# vim:fileencoding=utf-8
from django import forms
from django.shortcuts import render_to_response
from contents.models import FeedBack
from models import Robot


def robots(request):
    ctx = {'robots': Robot.objects.all()}
    return render_to_response('plugins/robots.txt', ctx, content_type="text/plain")


class FeedBackForm(forms.ModelForm):
    class Meta():
        model = FeedBack
        exclude = []
