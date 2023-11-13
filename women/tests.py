from http import HTTPStatus

from django.urls import reverse
from django.test import TestCase

from women.models import Women


class GetPageTestCase(TestCase):
    fixtures = ['women_women.json', 'women_category.json', 'women_husband.json', 'women_tagpost.json']

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

    def test_data_mainpage(self):
        w = Women.published.all().select_related('cat')
        path = reverse('home')
        response = self.client.get(path)

        self.assertQuerySetEqual(response.context_data['posts'], w[:5])

    def test_paginate_mainpage(self):
        path = reverse('home')
        pages = 1  # count all pages
        paginate_by = 5  # posts per page
        response = self.client.get(path + f'?page={pages}')
        w = Women.published.all().select_related('cat')

        self.assertQuerySetEqual(response.context_data['posts'], w[(pages-1)*paginate_by:pages*paginate_by])

    def test_content_post(self):
        w = Women.published.get(pk=1)
        path = reverse('post', args=[w.slug])
        response = self.client.get(path)

        self.assertEqual(w.content, response.context_data['post'].content)

    def tearDown(self):
        """Действия после выполнением каждого теста, например, очистка ресурсов"""
