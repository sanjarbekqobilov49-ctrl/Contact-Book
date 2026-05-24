from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, pagination, viewsets

from .models import Category, Contact
from .serializers import CategorySerializer, ContactSerializer


class StandardPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.annotate(
        contact_count=Count('contacts')
    ).all()
    serializer_class = CategorySerializer
    pagination_class = StandardPagination


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.select_related('category').all()
    serializer_class = ContactSerializer
    filter_backends = [
        DjangoFilterBackend, filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ['category']
    search_fields = ['full_name', 'phone', 'email']
    ordering_fields = ['full_name', 'created_at']
    ordering = ['-created_at']
    pagination_class = StandardPagination
