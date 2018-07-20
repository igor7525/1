from django.db import connection
from django.views.generic.base import TemplateView
from django.shortcuts import (get_object_or_404, render)
from django.template.response import TemplateResponse

from catalog.models import (Brand,Products)
from core.models import (Reviews, Banner, OurAdvantages, News, Logo)

# Create your views here.
def index(request):
	template_name = "index.html"

	best_offer = Products.objects.filter(best_offer=True, sold='0')

	context = {
		'banner_list': Banner.objects.filter(show=True),
		'review_list':  Reviews.objects.all().order_by('-created_at'),
		'best_offer': best_offer,
		'logo_list': Logo.objects.all().order_by('?'),
		'our_advantages': OurAdvantages.objects.all()
	}

	response = TemplateResponse(request, template_name, context)

	return response



class ContactsPageView(TemplateView):

	template_name = "contacts.html"
	print_template_name = "contacts-print.html"
	def get_template_names(self,):
	    if self.request and self.request.GET.get("print"):
		return [self.print_template_name, ]
	    return [self.template_name, ]

	def get_context_data(self, **kwargs):
		context = super(ContactsPageView, self).get_context_data(**kwargs)

		return context


def news_list(request):
	template_name = 'news/list.html'

	news_list = News.objects.all().order_by('-created_at')

	context = {
		'title': News._meta.verbose_name_plural,
		'news_list': news_list
	}

	response = TemplateResponse(request, template_name, context)

	return response


def news_detail(request, id):
	template_name = 'news/view_detail.html'

	object = get_object_or_404(News, id=id)

	context = {
		'model_verbose_name': News._meta.verbose_name_plural,
		'title': News._meta.verbose_name_plural,
		'object': object
	}

	response = TemplateResponse(request, template_name, context)

	return response
