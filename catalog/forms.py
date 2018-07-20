# coding=utf-8
from __future__ import unicode_literals
from constance import config
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _, get_language
from django import forms
from catalog.models import *
from django.conf import settings

class PrintForm(forms.ModelForm):
    class Meta:
	model = PrintRequest
	exclude = ["url"]

class RequestForm(forms.ModelForm):
    class Meta:
	model = CardRequest
	exclude = ["url"]

