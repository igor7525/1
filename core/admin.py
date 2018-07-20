# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from models import *
from django.db import models
from ckeditor_uploader.widgets import CKEditorUploadingWidget as CKEditorWidget
# codemirror

class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'admin_thumbnail', 'url', 'show')
    fields = ("title", "admin_thumbnail",'image','text', 'url', 'show')
    readonly_fields =['admin_thumbnail']
    list_display_links = ('title', 'admin_thumbnail')

admin.site.register(Banner, BannerAdmin)


class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'admin_thumbnail', "created_at")

    list_display_links = ('__unicode__', 'admin_thumbnail')

admin.site.register(Reviews, ReviewsAdmin)


class OurAdvantagesAdmin(admin.ModelAdmin):
    list_display = ('title', 'admin_thumbnail')

    list_display_links = ('title', 'admin_thumbnail')

admin.site.register(OurAdvantages, OurAdvantagesAdmin)


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title',)

    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget(attrs={'class': 'cked'})}
    }

admin.site.register(News, NewsAdmin)



class FlatPageCustom(FlatPageAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget(attrs={'class': 'cked'})}
    }

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageCustom)



class LogoAdmin(admin.ModelAdmin):
    list_display = ('name', 'admin_thumbnail')

    list_display_links = ('name', 'admin_thumbnail')

    fields = ('name', 'image')

admin.site.register(Logo, LogoAdmin)
