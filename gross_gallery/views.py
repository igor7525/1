from django.shortcuts import render
from django.template.response import TemplateResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from gross_gallery.models import ClientPhoto


def view_gallery(request):
    template_name = "gross_gallery/gallery.html"

    photos = ClientPhoto.objects.all()

    paginator = Paginator(photos, 20)
    page = request.GET.get('page')
    try:
        photos = paginator.page(page)
    except PageNotAnInteger:
        photos = paginator.page(1)
    except EmptyPage:
        photos = paginator.page(paginator.num_pages)

    context = {'photos': photos}

    return TemplateResponse(request, template_name, context)