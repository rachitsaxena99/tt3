import django_filters

from .models import *

class UnitFilter(django_filters.FilterSet):
    class Meta:
        model = Unit
        fields = ['subject','unitNo']