import django_filters

from .models import *

class DoubtFilter(django_filters.FilterSet):
    class Meta:
        model = Doubt
        fields = ['category']