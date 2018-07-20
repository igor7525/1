from __future__ import unicode_literals

from django import forms

from catalog.models import Products


from url_filter.filtersets import ModelFilterSet



class SpecialFilter(ModelFilterSet):
    class Meta:
        model = Products
        fields = ['char_brand', 'char_year_of_issue', "props"]


class TractiveUnitFilter(ModelFilterSet):
    class Meta:
        model = Products
        fields = ['char_brand', 'char_year_of_issue']


class TrailerFilter(ModelFilterSet):
    class Meta:
        model = Products
        fields = ['char_brand', 'char_year_of_issue']


class TruckFilter(ModelFilterSet):
    class Meta:
        model = Products
        fields = ['char_brand', 'char_year_of_issue']
