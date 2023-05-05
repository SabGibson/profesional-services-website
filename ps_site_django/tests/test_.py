from rest_framework.test import APIClient
from rest_framework import status
import pytest


@pytest.mark.django_db
class TestUserCreate:
    def test_if_user_created_via_endpoint_return_201(self):

        user = {
            'username': 'TestUserJoeBloggs',
            'password': 'MA&wAgl$lGudriG7mAwi',
            'first_name': 'Joseph',
            'last_name': 'Bloggs',
            'email': 'TestUserJoeBloggs@test.com'
        }

        client = APIClient()
        response = client.post('/api/v1/users/', user)
        print(response.data)
        assert response.status_code == status.HTTP_201_CREATED

    #     user = User.objects.get(username=user_data["username"])

    # # Check if the user was created successfully
    #     assert user is not None
    #     assert user.username == user_data["username"]
    #     assert user.email == user_data["email"]
    #     assert user.check_password(user_data["password"])
