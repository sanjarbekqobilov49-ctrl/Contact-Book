from rest_framework import serializers

from .models import Category, Contact


class CategorySerializer(serializers.ModelSerializer):
    contact_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'created_at', 'contact_count']


class ContactSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(
        source='category.name', read_only=True
    )

    class Meta:
        model = Contact
        fields = [
            'id', 'full_name', 'phone', 'email', 'image',
            'category', 'category_name', 'address', 'notes',
            'created_at', 'updated_at',
        ]
