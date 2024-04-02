from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient


class TeamViewTestCase(TestCase):
    def test_team_view(self):
        client = APIClient()
        response = client.get(reverse('game:team-view'), format='json')
        self.assertEqual(response.status_code, 200)
        print(response.data)


class UserViewTestCase(TestCase):
    def test_user_view(self):
        client = APIClient()
        response = client.post(reverse('game:user-view'), {'name': 'ПСЖ', 'score': '10'}, format='json')
        self.assertEqual(response.status_code, 200)
