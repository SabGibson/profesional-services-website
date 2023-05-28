from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Category, Product, ProductImage


class ProductImageSerializer(serializers.ModelSerializer):
    image_url = serializers.CharField(source='get_image', read_only=True)

    class Meta:
        model = ProductImage
        fields = ('id', 'image', 'image_url')


class ProductSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')
    category = 'CategorySerializer()'
    images = ProductImageSerializer(many=True, required=False)
    profile = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'name', 'creator', 'profile', 'slug', 'description',
                  'price', 'category', 'image', 'get_abs_url', 'get_image', 'get_thumbnail', 'images')

        read_only_fields = ('slug',)

    def get_profile(self, obj):
        return obj.creator.profile.id


class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = ("id", "name", "get_abs_url", "products")
