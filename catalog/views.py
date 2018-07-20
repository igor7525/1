# coding=utf-8
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from email_extras.utils import send_mail_template
from django.db.models import (Avg, Count, Max, Min)
from constance import config
from django.template import loader
from django.conf import settings
from django.contrib.sites.models import Site
from catalog.forms import RequestForm
from django.template.response import TemplateResponse
from django.http import (JsonResponse, HttpResponse, HttpResponseNotFound, Http404)
from django.shortcuts import (get_object_or_404, render)
from django.utils.translation import ugettext_lazy as _, get_language

from catalog.models import (SPECIAL_MODEL_SLUG, TRACTIVE_UNIT_MODEL_SLUG, TRAILER_MODEL_SLUG, TRUCK_MODEL_SLUG, Products, SLUG_LIST, Prop, PropItem)
from catalog.filters import (SpecialFilter, TractiveUnitFilter, TrailerFilter, TruckFilter)

MODELS = {
	SPECIAL_MODEL_SLUG: {'model': Products, 'filter': SpecialFilter},
	TRACTIVE_UNIT_MODEL_SLUG: {'model': Products, 'filter': SpecialFilter},
	TRAILER_MODEL_SLUG: {'model': Products, 'filter':SpecialFilter },
	TRUCK_MODEL_SLUG: {'model': Products, 'filter': SpecialFilter}
}

PAGE_SIZE = 20
ORPHANS = 3

# Create your views here.
def catalog_list(request, category):
	template_name = 'catalog/list.html'

	try:
		model = MODELS[category]['model']
	except KeyError as e:

		raise Http404(e)
	qs = model.objects.filter(slug=category)
	av_props = PropItem.objects.filter(in_filter=True)
	all_props = list(Prop.objects.filter(product_id__in=qs.values_list("pk", flat=True), propitem__in=av_props).order_by("propitem__order").values_list("value", "propitem__pk").distinct())
	prop_filter = []
	for p in av_props:
	 f = set(filter(lambda x: True if x[1] == p.pk else False, all_props))
	 if f:
	  prop_filter.append((p, f))
	year_interval = qs.aggregate(Min('char_year_of_issue'), Max('char_year_of_issue'))

	brand_list = qs.values('char_brand__name').order_by('char_brand').annotate(Avg('price'))

	year_list = list(qs.values('char_year_of_issue').annotate(Count('char_year_of_issue')).order_by('char_year_of_issue'))

	char_year_of_issue_chart = []
	for year in xrange(year_interval['char_year_of_issue__min'] or 0, year_interval['char_year_of_issue__max'] or 0):
		if year == year_list[0]['char_year_of_issue']:
			item = year_list.pop(0)
			char_year_of_issue_chart.append(['', item['char_year_of_issue__count']])
		else:
			char_year_of_issue_chart.append(['', 0])

	context = {
		'title': dict(SLUG_LIST).get(category),
		'category_slug': category,
		'brand_list': brand_list,
		'year_interval': year_interval,
		'prop_filter': prop_filter,
		'char_year_of_issue_chart': char_year_of_issue_chart
	}

	response = TemplateResponse(request, template_name, context)

	return response



def detail(request, category, id):
	template_name = 'catalog/view_detail.html'

	try:
		model = MODELS[category]['model']
	except KeyError as e:

		raise Http404(e)

	object = get_object_or_404(model, id=id)

	context = {
		'title': object.name,
		'category_name': model._meta.verbose_name_plural,
		'object': object,
		'related_list': model.objects.all().exclude(id=id).order_by('?')[:12]
	}
	form = RequestForm(request.POST or None)
	context.update(form=form)
	if form.is_valid():
	    inst = form.save(commit=False)
	    inst.url = "http://%s%s" % (request.get_host(), request.get_full_path())
	    inst.save()
	    email = form.cleaned_data.get("email")
	    
	    context.update(user_email = email, site=request.get_host(), phone=form.cleaned_data.get('phone'), text=form.cleaned_data.get('text'), request=request)
	    subject = _(u"%(site)s Карточка товара %(title)s") % context
	    if True:
	     send_mail_template(subject, 'truck_card', 
		settings.EMAIL_HOST_USER,
                email, 
		context=context)
	    if True and config.SEND_PRODUCT_CARD_COPY:
	        send_mail_template(subject, 'truck_card_copy', 
			settings.EMAIL_HOST_USER,	
	                config.FEEDBACK_EMAIL.replace(' ', '').split(','), 
			context=context)
	    return JsonResponse(dict(success=1))
	    # get template for maol
	    # Send email 
	if request.GET.get("print"):
	    template_name = "email_extras/truck_card.html"
	response = TemplateResponse(request, template_name, context)

	return response



def ajax(request, category):
	template_name = 'catalog/ajax_products.html'

	try:
		model = MODELS[category]['model']
		filter = MODELS[category]['filter']
	except KeyError as e:

		raise Http404(e)

	if request.is_ajax():
		queryset = model.objects.all().filter(slug=category).order_by('sold', '-id')

		order_by = request.GET.get('order_by')

		if order_by:
			try:
				queryset = queryset.order_by('sold', order_by)
			except Exception as e:
				pass

		object_list = filter(data=request.GET, queryset=queryset).filter()

		paginator = Paginator(object_list=object_list, per_page=PAGE_SIZE, orphans=ORPHANS)

		page = request.GET.get('page')

		try:
			products = paginator.page(page)
			
		except PageNotAnInteger:

			products = paginator.page(1)

		except EmptyPage:

			products = []

		next_page = 0
		if (products.has_next()):
			next_page = products.next_page_number()

		context = {
			'test': request.GET,
			'category': category,
			'object_list': products,
			'next_page': next_page
		}

		response = TemplateResponse(request, template_name, context)

		return response
