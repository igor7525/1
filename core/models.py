from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from django_thumbs.db.models import ImageWithThumbsField

# Create your models here.
# class User(AbstractUser):
#     avatar = ImageWithThumbsField(upload_to='avatar/%Y-%m-%d/', blank=True, null=True, sizes=((136, 136),))
#     position = models.CharField(_('position'), max_length=64, blank=True, null=True)
    
class Timestamps(models.Model):
	"""docstring for Timestamps"""
	created_at = models.DateTimeField(_('date of creation'), auto_now_add=True)
	updated_at = models.DateTimeField(_('last modification date'), auto_now=True)

	class Meta:
		abstract = True

class Reviews(models.Model):
	created_at = models.DateTimeField(_('date of creation'), )
	updated_at = models.DateTimeField(_('last modification date'), auto_now=True)
	first_name = models.CharField(_('first name'), max_length=30)
	last_name = models.CharField(_('last name'), max_length=30)
	review = models.TextField(_('review'))
	photo = ImageWithThumbsField(_('photo'), upload_to='review/%Y-%m-%d/', sizes=((128, 128),), default='default-avatar.128x128.jpg')

	class Meta:
		verbose_name = _('review')
		verbose_name_plural = _('reviews')

	def __unicode__(self):

		return _("%(first_name)s %(last_name)s") % {
			'first_name': self.first_name,
			'last_name': self.last_name,
			}

	def admin_thumbnail(self):
		if self.photo:

			return "<img src='%s' height='64px' style='border-radius: 50%%;' />" % (self.photo.thumbnail(128, 128))

		return "<div style='width: 64px; height: 64px; background: aliceblue; text-align: center; display: table-cell; vertical-align: middle; border-radius: 50%;'>No photo</div>"

	admin_thumbnail.short_description = _('photo')
	admin_thumbnail.allow_tags = True


class Banner(Timestamps):
	title = models.CharField(_('title'), max_length=64)
	text = models.TextField(_('text'))
	show = models.BooleanField(_('is show'), default=True)
	url = models.CharField(_('url'), max_length=128, default="/")

	image = ImageWithThumbsField(upload_to='banner/%Y-%m-%d/', sizes=((195, 64),))

	class Meta:
		verbose_name = _('banner')
		verbose_name_plural = _('banners')

	def admin_thumbnail(self):
		if self.image:

			return "<img src='%s' height='64px' />" % (self.image.thumbnail(195, 64))

		return "<div style='width: 195px; height: 64px; background: aliceblue; text-align: center; display: table-cell; vertical-align: middle;'>No photo</div>"

	admin_thumbnail.short_description = _('banner')
	admin_thumbnail.allow_tags = True


class OurAdvantages(Timestamps):
	"""docstring for OurAdvantages"""
	title = models.CharField(_('title'), max_length=64)
	description = models.TextField(_('description'))
	show = models.BooleanField(_('is show'), default=True)

	image = ImageWithThumbsField(_('image'), upload_to='advantages/%Y-%m-%d/', sizes=((64, 64),))

	class Meta:
		verbose_name = _('our advantages')
		verbose_name_plural = _('our advantages')

	def admin_thumbnail(self):
		if self.image:

			return "<img src='%s' height='64px' />" % (self.image.thumbnail(64, 64))

		return "<div style='width: 64px; height: 64px; background: aliceblue; text-align: center; display: table-cell; vertical-align: middle;'>No photo</div>"

	admin_thumbnail.short_description = _('image')
	admin_thumbnail.allow_tags = True

		


class News(Timestamps):
	title = models.CharField(_('title'), max_length=64)
	text = models.TextField(_('text'))

	miniature = ImageWithThumbsField(_('miniature'), upload_to='news/%Y-%m-%d/', blank=True, null=True, sizes=((298, 176),))

	class Meta:
		verbose_name = _('news')
		verbose_name_plural = _('news')

	def __unicode__(self):

		return _("%(title)s") % {'title': self.title}



class Logo(Timestamps):
	"""docstring for Logo"""
	name = models.CharField(_('name'), max_length=64)
	image = ImageWithThumbsField(_('image'), upload_to='core/logo/%Y-%m-%d/', sizes=((109, 62),))

	class Meta:
		verbose_name = _('logo')
		verbose_name_plural = _('logos')

	def __unicode__(self):

		return _("%(name)s") % {'name': self.name}

	def admin_thumbnail(self):
		if self.image:

			return "<img src='%s' height='62px' />" % (self.image.thumbnail(109, 62))

		return "<div style='width: 109px; height: 62px; background: aliceblue; text-align: center; display: table-cell; vertical-align: middle;'>No photo</div>"

	admin_thumbnail.short_description = _('image')
	admin_thumbnail.allow_tags = True
