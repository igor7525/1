from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser, Group
from django.utils.translation import ugettext_lazy as _

from django import forms
from django.db import models


from django_thumbs.db.models import ImageWithThumbsField

# Create your models here.
class User(AbstractUser):
    avatar = ImageWithThumbsField(upload_to='user/%Y-%m-%d/', blank=True, null=True, sizes=((136, 136),), default='default-avatar.136x136.jpg')
    position = models.CharField(_('position'), max_length=64, blank=True, null=True)
    phone = models.CharField(_('Phone'), max_length=64)
    phone_2 = models.CharField(_('Additional phone'), max_length=64, blank=True, null=True)



class Group(Group):

	class Meta:
		proxy = True

		verbose_name = _('group')
		verbose_name_plural = _('groups')
			