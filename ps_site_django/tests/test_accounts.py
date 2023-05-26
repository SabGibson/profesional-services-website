from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from accounts.models import *
from django.db import transaction
from model_bakery import baker
import pytest


@pytest.fixture
def create_user(api_client):
    def do_create_user(user_data):
        return api_client.post('/api/v1/users/', user_data)
    return do_create_user


@pytest.mark.django_db
class TestUserCreate:
    def test_if_user_created_via_endpoint_return_201(self, create_user):

        user_data = {
            'username': 'TestUserJoeBloggs',
            'password': 'MA&wAgl$lGudriG7mAwi',
            'first_name': 'Joseph',
            'last_name': 'Bloggs',
            'email': 'TestUserJoeBloggs@test.com'
        }

        response = create_user(user_data)
        print(response.data)
        assert response.status_code == status.HTTP_201_CREATED

    def test_if_profile_created_on_user_create_return_201(self, create_user):

        user = baker.make(User)
        profile = user.profile
        assert profile is not None


@pytest.mark.django_db
class TestUserEndpopints:
    def test_if_education_record_created_from_endpoint_return_201(self):
        api_client = APIClient()

        user = baker.make(User)
        api_client.force_authenticate(user=user)

        record_data = {
            "level": "PhD",
            "institution_name": "Oxford University",
            "qualification_name": "Doctor of Philosophy in Computer Science",
            "description": "Research in Artificial Intelligence",
            "date_achieved": "2022-12-12"
        }

        response = api_client.post(
            '/api/v1/profile-education/', data=record_data)
        assert response.status_code == status.HTTP_201_CREATED
