from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class RegisterUserTestCase(TestCase):
    def setUp(self):
        self.data = {
            'username': 'user_1',
            'email': 'user1@sitewomen.ru',
            'first_name': 'Sergey',
            'last_name': 'Balakirev',
            'password1': '12345678Aa',
            'password2': '12345678Aa',
        }

    def test_form_registration_get(self):
        path = reverse('users:register')
        response = self.client.get(path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'users/register.html')

    def test_user_registration_success(self):
        user_model = get_user_model()
        path = reverse('users:register')
        response = self.client.post(path, self.data)

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse('users:login'))  # check for a suitable redirects
        self.assertTrue(user_model.objects.filter(username=self.data['username']).exists())  # check a new user in DB

    def test_user_registration_password_error(self):
        self.data['password2'] = '12345678A'
        path = reverse('users:register')
        response = self.client.post(path, self.data)

        self.assertEqual(response.status_code, HTTPStatus.OK)  # no redirect
        self.assertContains(response, 'Введенные пароли не совпадают')

    def test_user_registration_exists_error(self):
        user_model = get_user_model()
        user_model.objects.create(username=self.data['username'])

        path = reverse('users:register')
        response = self.client.post(path, self.data)
        self.assertEqual(response.status_code, HTTPStatus.OK)  # no redirect
        self.assertContains(response, 'Пользователь с таким именем уже существует')
