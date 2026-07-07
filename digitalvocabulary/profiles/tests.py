from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase


class RegisterViewTests(APITestCase):
    def test_register_user_with_valid_data(self):
        url = reverse('register')
        payload = {
            'username': 'jane',
            'email': 'jane@example.com',
            'password': 'StrongPass123!'
        }

        response = self.client.post(url, payload, format='json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['username'], 'jane')
        self.assertEqual(response.data['email'], 'jane@example.com')
        self.assertTrue(get_user_model().objects.filter(username='jane').exists())
