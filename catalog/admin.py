# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from django.db import models
from django.forms.widgets import CheckboxSelectMultiple, RadioSelect
from django.utils.translation import ugettext_lazy as _
from ckeditor_uploader.widgets import CKEditorUploadingWidget as CKEditorWidget

from adminsortable.admin import NonSortableParentAdmin, SortableStackedInline, SortableAdmin

# Register your models here.
from catalog.models import (Prop,
    Equipment, Color, Brand, VehicleType, PropItem,
    CardRequest, PrintRequest,
    Products, Photo, WheelArrangement, GearboxType)

class ProppAdmin(SortableAdmin):
    list_display = ["pk", "name", "slug", "in_filter"]
    list_editable = ["name", "slug","in_filter" ]
    ordering = ["order", ]
    prepopulated_fields = {
	"slug": ["name", ]
	}

class PropAdmin(admin.ModelAdmin):
    list_display = ["pk", "name", "slug", ]
    list_editable = ["name", "slug", ]
    prepopulated_fields = {
	"slug": ["name", ]
	}

#admin.site.register(WheelArrangement, PropAdmin)
admin.site.register(PropItem, ProppAdmin)
#admin.site.register(GearboxType, PropAdmin)

class HideAppAdmin(admin.ModelAdmin):

    def get_model_perms(self, request):

        return {}


admin.site.register(Equipment)
admin.site.register(Color, HideAppAdmin)
admin.site.register(VehicleType, HideAppAdmin)
from django.utils.safestring import mark_safe

class RequestAdmin(admin.ModelAdmin):
    list_display = ('email',"phone","text","link", "created")
    list_filter =["created",]
    readonly_fields = ["email", "phone", "text", "link", "url"]
    fields = ["email", "phone", "text", "link"]

    def link(self, obj=None):
	if obj:
	 from catalog.views import *
	 from urlparse import urlparse
	 p = urlparse(obj.url).path.strip("/").split('/')
	 try:
	  model = MODELS[p[1]]["model"]
	  name = model.objects.get(pk=p[2].split('-')[-1]).name
	 except:
	  name = obj.url
	 return mark_safe("<a href='%s'>%s</a>" % (obj.url, name))
	return ''

admin.site.register(CardRequest, RequestAdmin)
#admin.site.register(PrintRequest, RequestAdmin)


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'admin_thumbnail')

    list_display_links = ('name', 'admin_thumbnail')

    fields = ('name', 'image')

admin.site.register(Brand, BrandAdmin)



class SpecialAdminForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = '__all__'
        widgets = {
          'description': CKEditorWidget(attrs={'class': 'ckedit'}),
        }


class PropSAdmin(SortableStackedInline):
	model = Prop
	extra = 3

class SpecialPhotoInline(SortableStackedInline):
    model = Photo
    extra = 5

class SpecialAdmin(NonSortableParentAdmin):
    list_display = ('admin_thumbnail', 'name', "slug",'char_vehicle_type', 'best_offer', 'get_price', 'user')

    list_display_links = ('admin_thumbnail', 'name')

    search_fields = ['name', 'char_brand__name']

    list_filter = ("slug", 'char_brand', 'best_offer', 'user')
    filter_horizontal = ['related', "related_same", "equipment"]

    fieldsets = (
        (None, {
            'fields': (('name', "slug",), 'short_description', 'description', ('price', 'sold'), ('best_offer', 'stock'), ('new_offer', 'sale_offer'), "equipment",'related', 'related_same')
        }),
        (None, {
            'fields': ('user',),
        }),
        (_('Characteristic'), {
            'fields': (
                ('char_brand', 'char_model', 'char_year_of_issue'),
                ('char_vehicle_type', 'char_colour', "char_mileage"),
            )
        }),
        (_('Video'), {
            'fields': ('video',),
        })
    )

    form = SpecialAdminForm

    inlines = [
	PropSAdmin,
        SpecialPhotoInline,
    ]

admin.site.register(Products, SpecialAdmin)
