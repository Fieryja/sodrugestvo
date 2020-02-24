# vim:fileencoding=utf-8
from django.contrib import admin
from sodrugestvo.utils import copy_object
from .models import News, Robot, FeedBack, Block


class NewsAdmin(admin.ModelAdmin):
    actions = [copy_object]
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ['name']
    list_display = ['name', 'active', 'date']
    list_editable = ['active']


class FeedBackAdmin(admin.ModelAdmin):
    list_display = ['name', 'date']


class BlockAdmin(admin.ModelAdmin):
    list_display = ['name', 'comment']


admin.site.register(FeedBack, FeedBackAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Block, BlockAdmin)
admin.site.register(Robot)