import django_filters

from .models import Contact


class ContactFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='filter_search')
    category = django_filters.NumberFilter(field_name='category_id')

    class Meta:
        model = Contact
        fields = ['category']

    def filter_search(self, queryset, name, value):
        return queryset.filter(
            full_name__icontains=value
        ) | queryset.filter(phone__icontains=value) | queryset.filter(
            email__icontains=value
        )
