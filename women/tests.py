from http import HTTPStatus

from django.urls import reverse
from django.test import TestCase


class GetPageTestCase(TestCase):
    def setUp(self):
        """Инициализация перед выполнением каждого теста"""

    def test_mainpage(self):
        path = reverse('home')
        response = self.client.get(path)  # imitating GET query to `path`

        self.assertEqual(response.status_code, HTTPStatus.OK)  # check status code
        self.assertTemplateUsed(response, 'women/index.html')  # check response templates contain `index.html`
        self.assertEqual(response.context_data['title'], 'Главная страница')

    def test_redirect_addpage(self):
        path = reverse('add_page')
        redirect_uri = reverse('users:login') + '?next=' + path
        response = self.client.get(path)

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, redirect_uri)  # check response redirects to redirect_uri

    def tearDown(self):
        """Действия после выполнением каждого теста, например, очистка ресурсов"""
