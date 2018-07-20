# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from adminsortable.models import SortableMixin
from django_thumbs.db.models import ImageWithThumbsField
from django.utils.translation import ugettext_lazy as _
import uuid


def get_photos_folder(self, filename):
    """ переименовываем загружаемый файл """

    _end = filename.split('.')[-1]
    name = str(uuid.uuid4())[:8]
    return u'gross_gallery/{}.{}'.format(name, _end)


class ClientPhoto(SortableMixin):
    image = ImageWithThumbsField(_('image'), upload_to=get_photos_folder, sizes=((250, 150), (64, 64)))
    description = models.TextField(_('description'))
    order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    class Meta:
        ordering = ["order", ]
        verbose_name = _('photo')
        verbose_name_plural = _('photo')

    def __unicode__(self):
        return _("%(image)s") % {'image': self.image.url}

    @property
    def get_short_description(self):
        if len(self.description) > 200:
            return self.description[:201] + '...'
        else:
            return self.description

    def view_photo(self):
        return "<img src='%s' height='64px' />" % (self.image.thumbnail(64, 64))

    @property
    def middle_photo(self):
        return self.image.thumbnail(250, 150)