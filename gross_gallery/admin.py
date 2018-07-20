# -*- coding: utf-8 -*-

from django.contrib import admin
from adminsortable.admin import SortableStackedInline, SortableAdmin
from gross_gallery.models import ClientPhoto


class ClientPhotoAdmin(SortableAdmin):
    model = ClientPhoto
    list_display = ('view_photo', 'get_short_description')
    list_display_links = ('view_photo', 'get_short_description')
    search_fields = ('description', )
    sortable_change_list_template = 'admin/gross_gallery/change_list.html'

    def view_photo(self, obj):
        return "<img src='%s' height='64px' />" % (obj.image.thumbnail(64, 64))

    view_photo.short_description = 'Photo'
    view_photo.allow_tags = True

    def get_short_description(self, obj):
        return obj.get_short_description

    get_short_description.short_description = 'Description'


admin.site.register(ClientPhoto, ClientPhotoAdmin)