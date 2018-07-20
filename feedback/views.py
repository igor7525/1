# -*- coding: utf-8 -*-
import json

from django.views.generic import CreateView
from django.conf import settings
from django.http import HttpResponse
from django.contrib.sites.models import Site
from django.core.mail import (send_mail, EmailMultiAlternatives)
from django.utils.translation import ugettext as _

from constance import config

from feedback.models import TYPE_LIST
from feedback.forms import FeedbackForm



class FeedbackView(CreateView):
    form_class = FeedbackForm
    template_name = 'feedback/feedback.html'

    def get_form_kwargs(self):
        kwargs = super(FeedbackView, self).get_form_kwargs()
        if 'data' in kwargs:
            post = kwargs['data'].copy()
            post['url'] = self.kwargs['url']
            post['site'] = Site.objects.get_current().pk
            kwargs['data'] = post
        return kwargs

    def get_success_url(self):
        return self.kwargs['url']

    def form_valid(self, form):
        response = super(FeedbackView, self).form_valid(form)

        if config.FEEDBACK_EMAIL != '':
            d = form.cleaned_data
	    ts = d.get("form_type", "write")
	    tp = dict(TYPE_LIST).get(ts)
            message = (
                u'Имя: %(name)s',
                u'Имя: %(name)s'
            )

            try:
                subject = u'"%(type)s" с сайта %(host)s' % ({
                    'host': self.request.get_host(),
		    'type': tp
                    })
                text_content = u'Имя: %(name)s; Номер телефона: %(phone)s; Подробнее %(host)s/admin/feedback/feedback/' % ({
                    'host': self.request.get_host(),
                    'name': d['name'],
                    'phone': d['phone']
                })
                html_content = u'<p>URL: <a href="%(host)s%(url)s" target="_blank">%(host)s%(url)s</a>;</p><p>Имя: %(name)s;</p><p>Номер телефона: %(phone)s;</p><p>Сообщение: %(text)s;</p><p><a href="http://%(host)s/admin/feedback/feedback/">Перейти в админ панель</a></p>' % ({
                    'host': self.request.get_host(),
                    'url': d['url'],
                    'name': d['name'],
                    'text': d.get('text', ''),
                    'phone': d['phone'],
                })
		emails = getattr(config, ts.replace("-", "_"), config.FEEDBACK_EMAIL)
		if not emails:
		    emails = config.FEEDBACK_EMAIL
                msg = EmailMultiAlternatives(
                    subject,
                    text_content,
                    settings.EMAIL_HOST_USER,
                    emails.replace(' ', '').split(',')
		)

                msg.attach_alternative(html_content, "text/html")
                msg.send()
            except:

                return HttpResponse(json.dumps({'error': _('Failed to send email')}))

        return HttpResponse(json.dumps({}))

    def form_invalid(self, form):
        
        return HttpResponse(json.dumps({'errors': form.errors}))

