# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import locale

from datetime import datetime

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _


from django_thumbs.db.models import ImageWithThumbsField

SOLD_CHOICES = (
    ('1', _('Yes')),
    ('0', _('No'))
)

COMMON_CHOICES_YES = u'Да'
COMMON_CHOICES_NO = ''
COMMON_CHOICES_DEFAULT = COMMON_CHOICES_NO
COMMON_CHOICES = (
    (COMMON_CHOICES_YES, _('Yes')),
    (COMMON_CHOICES_NO, _('No'))
)


GEARBOX_TYPE_MANUAL = u"МКПП"
GEARBOX_TYPE_AUTOMATIC = u"АКПП"

GEARBOX_TYPE_LIST = (
	(GEARBOX_TYPE_MANUAL, _(u"МКПП")),
	(GEARBOX_TYPE_AUTOMATIC, _(u"АКПП"))
)

WHEEL_ARRANGEMENT_4_2 = "4x2"
WHEEL_ARRANGEMENT_4_4 = "4x4"
WHEEL_ARRANGEMENT_6_4 = "6x4"
WHEEL_ARRANGEMENT_6_6 = "6x6"
WHEEL_ARRANGEMENT_8_4 = "8x4"

WHEEL_ARRANGEMENT_LIST = (
	(WHEEL_ARRANGEMENT_4_2, ("4x2")),
	(WHEEL_ARRANGEMENT_4_4, ("4x4")),
	(WHEEL_ARRANGEMENT_6_4, ("6x4")),
	(WHEEL_ARRANGEMENT_6_6, ("6x6")),
	(WHEEL_ARRANGEMENT_8_4, ("8x4")),
)


SPECIAL_MODEL_SLUG = "special"
TRACTIVE_UNIT_MODEL_SLUG = "tractive-unit"
TRAILER_MODEL_SLUG = "trailer"
TRUCK_MODEL_SLUG = "truck"
SLUG_LIST = [
(SPECIAL_MODEL_SLUG,"Спецтехника"),
(TRACTIVE_UNIT_MODEL_SLUG,"Тягачи"),
(TRAILER_MODEL_SLUG,"Полуприцепы"),
(TRUCK_MODEL_SLUG,"Грузовики"),
]
from django.core.cache import caches
cache = caches["default"]


# Create your models here.
class Timestamps(models.Model):
	"""docstring for Timestamps"""
	created_at = models.DateTimeField(_('date of creation'), auto_now_add=True)
	updated_at = models.DateTimeField(_('last modification date'), auto_now=True)

	def save(self, *args, **kwargs):
	    cache.delete(self.get_class_key())
	    super(Timestamps, self).save(*args, **kwargs)

	class Meta:
		abstract = True

	@classmethod
	def get_class_key(cls):
	    return u"%s:%s" % ("class",cls.__name__)
	
	@classmethod
	def get_selects(cls, defaults):
	    #return defaults
	    cv = cache.get(cls.get_class_key())
	    if not cv:
		try:
		 cv = cls.objects.all().values_list("slug", "name")
		except:
		 cv = defaults
	    return cv

class GearboxType(Timestamps):
	name = models.CharField(_('name'), max_length=64)
	slug = models.SlugField(_('slug'), max_length=64)

	class Meta:
		verbose_name = _('gearbox type')
		verbose_name_plural = _('gearbox types')

	def __unicode__(self):
		return _("%(name)s") % {'name': self.name}

class WheelArrangement(Timestamps):
	name = models.CharField(_('name'), max_length=64)
	slug = models.SlugField(_('slug'), max_length=64)

	class Meta:
		verbose_name = _('wheel arrangement')
		verbose_name_plural = _('wheel arrangements')

	def __unicode__(self):

		return _("%(name)s") % {'name': self.name}
GEARBOX_TYPE_LIST = GearboxType.get_selects(GEARBOX_TYPE_LIST)
WHEEL_ARRANGEMENT_LIST = WheelArrangement.get_selects(WHEEL_ARRANGEMENT_LIST)

class Equipment(Timestamps):
	name = models.CharField(_('name'), max_length=64)

	class Meta:
		verbose_name = _('equipment')
		verbose_name_plural = _('equipments')

	def __unicode__(self):

		return _("%(name)s") % {'name': self.name}



class Color(Timestamps):
	name = models.CharField(_('name'), max_length=64)

	class Meta:
		verbose_name = _('color')
		verbose_name_plural = _('colors')

	def __unicode__(self):

		return _("%(name)s") % {'name': self.name}
from adminsortable.models import SortableMixin

class PropItem(Timestamps, SortableMixin):
	name = models.CharField(_('name'), max_length=64)
	slug = models.SlugField(_('slug'), max_length=64)
	in_filter = models.BooleanField(_('in filter?'), default=False)
	order = models.PositiveIntegerField(default=0, editable=False, db_index=True)
	
	class Meta:
		verbose_name = _('характеристика')
		ordering = ["order", ]
		verbose_name_plural = _('характеристики')

	def __unicode__(self):
		return _("%(name)s") % {'name': self.name}

class Prop(Timestamps, SortableMixin):
	propitem = models.ForeignKey("PropItem",verbose_name=_('characteristic'), )
	value = models.CharField(_('value'), max_length=255)
	order = models.PositiveIntegerField(default=0, editable=False, db_index=True)
	product = models.ForeignKey("Products", verbose_name=_("Техника"), related_name="props")
	def characteristic(self):
		return self.propitem.name
	class Meta:
		verbose_name = _('characteristic')
		verbose_name_plural = _('characteristics')
		ordering = ["order", ]

	def __unicode__(self):
		return _("%(name)s") % {'name': self.characteristic()}
def get_dir_name_cat(self, filename):
    _end = filename.split('.')[-1]
    import uuid
    name = str(uuid.uuid4())[:8]
    return u'catalog/photos/{}.{}'.format(name, _end)

class Photo(Timestamps, SortableMixin):
	image = ImageWithThumbsField(_('image'), upload_to=get_dir_name_cat, sizes=((298, 176), (64, 64)))
	product = models.ForeignKey("Products", verbose_name=_('photo'), related_name='photos')
	order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

	class Meta:
		ordering = ["order", ]
		verbose_name = _('photo')
		verbose_name_plural = _('photo')

	def __unicode__(self):

		return _("%(image)s") % {'image': self.image.url}
class Characteristic(models.Model):
	char_brand = models.ForeignKey("Brand", verbose_name=_('brand'), on_delete=models.PROTECT)
	char_model = models.CharField(_('model'), max_length=64, blank=True, null=True)
	char_mileage =  models.CharField(_('пробег'), max_length=64, blank=True)
	char_vehicle_type = models.ForeignKey("VehicleType", verbose_name=_('vehicle type'), on_delete=models.PROTECT)
	char_year_of_issue = models.PositiveSmallIntegerField(_('year of issue'))
	char_colour = models.ForeignKey("Color", verbose_name=_('colour'), blank=True, null=True, on_delete=models.SET_NULL)

	class Meta:
		abstract = True

		verbose_name = _('Характеристика')
		verbose_name_plural = _('Характеристики')

	def get_brand(self):

		return self.char_brand

	def get_color(self):

		return self.char_colour

	def get_vehicle_type(self):

		return self.char_vehicle_type

	def get_engine_power(self):

		return _("%(horsepower)s HP (%(kw)s kW)") % {
			'horsepower': self.char_engine_power,
			'kw': (self.char_engine_power * 0.74)
		}

	def get_trailer_type(self):
		
		return self.char_trailer_type

	def get_characteristic(self):
		characteristic_list = []
		for i in ["char_brand", "char_model", "char_vehicle_type", "char_year_of_issue", "char_colour", "char_mileage"]:
			v = getattr(self, i, None)
			if v:
				characteristic_list.append(dict(characteristic=self._meta.get_field(i).verbose_name, value=v))
		props = list(self.props.all())
		return characteristic_list + props
		fields = self._meta.get_fields()
		return characteristic_list

class Products(Timestamps, Characteristic):
    """docstring for Products"""

    name = models.CharField(_('name'), max_length=64)
    slug = models.CharField(_('Категория'), max_length=20, choices=SLUG_LIST, db_index=True)
    short_description = models.CharField(_('short description'), max_length=124, blank=True, null=True)
    description = models.TextField(_('description'))
    price = models.PositiveIntegerField(_('price'))

    best_offer = models.BooleanField(_('best offer'), default=False)
    video = models.CharField(_('video id'), max_length=250, blank=True, null=True)
    stock = models.BooleanField(_('stock'), default=False)
    sold = models.CharField(_('sold'), max_length=1, choices=SOLD_CHOICES, default='0')
    new_offer = models.BooleanField(_('new'), default=False)
    sale_offer = models.BooleanField(_('sale'), default=False)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('user'), default=1, on_delete=models.PROTECT)

    trashed_at = models.DateTimeField(blank=True, null=True)
	
    display_price = property(lambda self: locale.currency(int(self.price), grouping=True))
    related = models.ManyToManyField('self', blank=True, verbose_name=_(u"так же покупают"))
    related_same = models.ManyToManyField('self', blank=True, verbose_name=_(u"похожие товары"))
    equipment = models.ManyToManyField("Equipment", verbose_name=_('equipment'), blank=True)

    class Meta:
        verbose_name = _('Техника')
        verbose_name_plural = _('Техника')

    def __unicode__(self):
        return _("%(name)s") % {'name': self.name}

    def delete(self, trash=True):
        if not self.trashed_at and trash:
            self.trashed_at = datetime.now()
            self.save()

        else:
            super(Products, self).delete()

    def restore(self, commit=True):
        self.trashed_at = None

        if commit:
            self.save()

    def get_price(self):

        return (u"%s р." % (self.price))

    get_price.short_description = _('price')

    def admin_thumbnail(self):
        if self.photos.all().exists():

            return "<img src='%s' height='64px' />" % (self.photos.first().image.thumbnail(64, 64))

        return "<div style='width: 64px; height: 64px; background: aliceblue; text-align: center; display: table-cell; vertical-align: middle;'>Нет фото</div>"

    admin_thumbnail.short_description = _('image')
    admin_thumbnail.allow_tags = True



class Brand(Timestamps):
	"""docstring for Brand"""
	name = models.CharField(_('name'), max_length=64)
	image = ImageWithThumbsField(_('image'), upload_to='catalog/brands/%Y-%m-%d/', null=True, blank=True, sizes=((109, 62),))

	class Meta:
		verbose_name = _('brand')
		verbose_name_plural = _('brands')

	def __unicode__(self):

		return _("%(name)s") % {'name': self.name}

	def admin_thumbnail(self):
		if self.image:

			return "<img src='%s' height='62px' />" % (self.image.thumbnail(109, 62))

		return "<div style='width: 109px; height: 62px; background: aliceblue; text-align: center; display: table-cell; vertical-align: middle;'>Нет фото</div>"

	admin_thumbnail.short_description = _('image')
	admin_thumbnail.allow_tags = True


class VehicleType(Timestamps):
	"""docstring for VehicleType"""
	name = models.CharField(_('name'), max_length=64)

	class Meta:
		verbose_name = _('vehicle type')
		verbose_name_plural = _('vehicle types')

	def __unicode__(self):

		return _("%(name)s") % {'name': self.name}




class PrintRequest(models.Model):
    url = models.CharField(max_length=255, verbose_name=_('url'))
    email = models.EmailField(verbose_name=_('email'))
    phone = models.CharField(max_length=32, verbose_name=_('phone'), blank=True)
    text = models.TextField(verbose_name=_('text'), blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __unicode__(self):
        return u'{url}: {email}'.format(url=self.url, email=self.email)

    class Meta:
	verbose_name = _(u'Печать КП')
	verbose_name_plural = _(u'Печать КП')

class CardRequest(models.Model):
    url = models.CharField(max_length=255, verbose_name=_('url'))
    email = models.EmailField(verbose_name=_('email'))
    phone = models.CharField(max_length=32, verbose_name=_('phone'), blank=True)
    text = models.TextField(verbose_name=_('text'), blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __unicode__(self):
        return u'{url}: {email}'.format(url=self.url, email=self.email)

    class Meta:
	verbose_name = _(u'Запрос КП')
	verbose_name_plural = _(u'Запрос КП')
