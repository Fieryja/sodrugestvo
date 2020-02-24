from codemirror2.widgets import CodeMirrorEditor
from django import forms
from django.contrib import admin
from sodrugestvo.utils import copy_object
from models import FeedBack, Service, Blog


admin.site.register(Blog)
admin.site.register(Service)


class FeedAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'date']


admin.site.register(FeedBack, FeedAdmin)
