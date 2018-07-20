# coding: utf-8
from __future__ import unicode_literals
from django.db import models
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _

TYPE_LIST = [
("call","Заказ звонка"),
("write","Напишите нам"),
("leasing","Лизинг"),
("print","Печать КП"),
("watch","Заявка на просмотр КП"),
("request","Запрос КП"),
("to_mail","Отправка на почту КП"),
("credit-leasing","Кредит-Лизинг КП"),
("why-leasing","Почему лизинг?"),
("why-credit","Почему кредит?"),
]
class Feedback(models.Model):
    site = models.ForeignKey(Site, verbose_name=_('site'))
    url = models.CharField(max_length=255, verbose_name=_('url'))
    urlhash = models.TextField(verbose_name=_('urlhash'), default="", null=True, blank=True)
    useragent = models.TextField(verbose_name=_('useragent'), default="", null=True, blank=True)
    name = models.CharField(max_length=32, verbose_name=_('first name'))
    form_type = models.CharField(max_length=32, verbose_name=_('Форма'), choices=TYPE_LIST, default="write")
    phone = models.CharField(max_length=32, verbose_name=_('phone'))
    subject = models.CharField(max_length=255, blank=True, null=True,
            verbose_name=_('subject'))
    email = models.EmailField(blank=True, null=True, verbose_name=_('email'))
    text = models.TextField(verbose_name=_('text'), blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __unicode__(self):
        return u'{url}: {subject}'.format(url=self.url, subject=self.subject)
