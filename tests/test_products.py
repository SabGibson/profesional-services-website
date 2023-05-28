import pytest
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User, AnonymousUser
from products.models import Product, Category
from django.urls import reverse
from model_bakery import baker


@pytest.fixture
def create_product(api_client):
    def do_create_product(product_data):
        return api_client.post('/api/v1/product-admin/', product_data)
    return do_create_product


@pytest.mark.django_db
class TestProductCreate:

    def test_create_product_with_authenticated_user_return_2xx_created(self, api_client):

        user = baker.make(User)
        api_client = APIClient()
        api_client.force_authenticate(user=user)

        category = baker.make(Category)

        data = {
            'creator': user.id,
            'category': category.id,
            'name': 'Test Product',
            'slug': 'test-product',
            'description': 'This is a test product',
            'price': 9.99,
        }

        response = api_client.post(
            '/api/v1/product-admin/', data=data, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert Product.objects.filter(name=data['name']).exists()

    def test_create_product_with_anonymus_user_return_4xx_forbidden(self, api_client):

        user = baker.make(User)
        category = baker.make(Category)

        data = {
            'creator': user.id,
            'category': category.id,
            'name': 'Test Product',
            'slug': 'test-product',
            'description': 'This is a test product',
            'price': 9.99,
        }

        response = api_client.post(
            '/api/v1/product-admin/', data=data, format='json')
        assert response.status_code == status.HTTP_403_FORBIDDEN
        assert not Product.objects.filter(name=data['name']).exists()


@pytest.mark.django_db
class TestProductUpdate:

    def test_update_product_with_authenticated_creator_return_2xx_ok(self, api_client):

        creator = baker.make(User)
        api_client.force_authenticate(user=creator)
        product = baker.make(Product, creator=creator)

        data = {
            'name': 'Test Product Updated'
        }

        response = api_client.patch(
            f'/api/v1/product-admin/{product.id}/', data=data, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert Product.objects.get(id=product.id).name == data['name']

    def test_update_product_with_authenticated_user_return_4xx_forbidden(self, api_client):

        creator = baker.make(User)
        user = baker.make(User)
        product = baker.make(Product, creator=creator)
        api_client.force_authenticate(user=user)

        data = {
            'name': 'Test Product Updated'
        }

        response = api_client.patch(
            f'/api/v1/product-admin/{product.id}/', data=data, format='json')
        assert response.status_code == status.HTTP_403_FORBIDDEN
        assert Product.objects.get(id=product.id).name != data['name']

    def test_update_product_with_anonymus_user_return_4xx_forbidden(self, api_client):

        creator = baker.make(User)
        product = baker.make(Product, creator=creator)

        data = {
            'name': 'Test Product Updated'
        }

        response = api_client.patch(
            f'/api/v1/product-admin/{product.id}/', data=data, format='json')
        assert response.status_code == status.HTTP_403_FORBIDDEN
        assert Product.objects.get(id=product.id).name != data['name']


@pytest.mark.django_db
class TestProductRead:

    def test_read_product_with_anonymus_creator_return_2xx_ok(self, api_client):

        product = baker.make(Product)

        response = api_client.get(
            f'/api/v1/products/{product.category.slug}/{product.slug}/')
        assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
class TestProductDelete:

    def test_delete_product_with_authenticated_creator_return_2xx_no_content(self, api_client):

        creator = baker.make(User)
        api_client.force_authenticate(user=creator)
        product = baker.make(Product, creator=creator)

        response = api_client.delete(
            f'/api/v1/product-admin/{product.id}/')
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert not Product.objects.filter(id=product.id).exists()

    def test_deletee_product_with_authenticated_user_return_4xx_forbidden(self, api_client):

        creator = baker.make(User)
        user = baker.make(User)
        product = baker.make(Product, creator=creator)
        api_client.force_authenticate(user=user)

        response = api_client.patch(
            f'/api/v1/product-admin/{product.id}/')
        assert response.status_code == status.HTTP_403_FORBIDDEN
        assert Product.objects.filter(id=product.id).exists()

    def test_update_product_with_anonymus_user_return_4xx_forbidden(self, api_client):

        creator = baker.make(User)
        product = baker.make(Product, creator=creator)

        response = api_client.delete(
            f'/api/v1/product-admin/{product.id}/')
        assert response.status_code == status.HTTP_403_FORBIDDEN
        assert Product.objects.filter(id=product.id).exists()
