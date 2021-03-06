import django_filters
from django_filters import CharFilter

from .models import Item


class ItemFilter(django_filters.FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Item
        fields = ['title']
