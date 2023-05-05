from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Category, Product, ProductImage


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "name", "get_abs_url", "description",
                  "price", "get_image", "get_thumbnail",)


class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = ("id", "name", "get_abs_url", "products")


class ProductImageSerializer(serializers.ModelSerializer):
    image_url = serializers.CharField(source='get_image', read_only=True)

    class Meta:
        model = ProductImage
        fields = ('id', 'image', 'image_url')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class ProductSerializer(serializers.ModelSerializer):
    creator = UserSerializer(read_only=True)
    category = CategorySerializer()
    images = ProductImageSerializer(many=True, required=False)

    class Meta:
        model = Product
        fields = ('id', 'name', 'slug', 'description',
                  'price', 'category', 'image', 'get_abs_url', 'get_image', 'get_thumbnail', 'images')

    def create(self, validated_data):
        images_data = validated_data.pop('images', [])
        category_data = validated_data.pop('category')
        category, _ = Category.objects.get_or_create(**category_data)
        creator = self.context['request'].user
        product = Product.objects.create(
            creator=creator, category=category, **validated_data)
        for image_data in images_data:
            ProductImage.objects.create(product=product, **image_data)
        return product
