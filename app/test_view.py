from .view import logout

from django.test import RequestFactory
from django.test import TestCase


class TestUserSession(TestCase):

    def test_get(self):
        response = self.client.get('')
        self.assertTemplateUsed(response, 'index.html')
        assert response.status_code == 200

    def test_logout(self):
        response = self.client.get('/logout')
        assert response.status_code == 302
