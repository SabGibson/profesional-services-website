from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product, Category
from rest_framework.permissions import IsAuthenticated
from .serializers import ProductSerializer, CategorySerializer
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework import status
from .permissions import IsCreatorOrReadOnly
from django.db.models import Q


class LatestProductsLists(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()[:4]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductDetail(APIView):
    def get_object(self, category_slug, product_slug):
        try:
            return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, product_slug, format=None):
        product = self.get_object(category_slug, product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


class CategoryDetail(APIView):

    def get_object(self, category_slug):
        try:
            return Category.objects.get(slug=category_slug)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, format=None):
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)


class ProductViewSet(viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsCreatorOrReadOnly]

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(creator=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, pk=None):
        product = self.get_object()
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def search(request):
    query = request.data.get('query', '')

    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query))
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    else:
        return Response({"products": []})
