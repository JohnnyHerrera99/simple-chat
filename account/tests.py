from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class RegistrationTestCase(TestCase):

    def test_registration_form_valid(self):
        form_data = {
            'username': 'john1234',
            'first_name': 'John',
            'last_name': 'Lennon',
            'email': 'jhon4@beatles.com',
            'password1': '1mag1n3a',
            'password2': '1mag1n3a',
        }
        response = self.client.post(reverse('register'), data=form_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/")
        self.assertTrue(User.objects.filter(username=form_data["username"]).exists())

    def test_registration_form_invalid(self):
        form_data = {
            'username': '',
            'first_name': 'John',
            'last_name': 'Lennon',
            'email': 'jhon4@beatles.com',
            'password1': '1mag1n3a',
            'password2': '1mag1n3allp30pl3',
        }

        response = self.client.post(reverse('register'), data=form_data)

        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'username', 'This field is required.')
        self.assertFormError(response, 'form', 'password2', 'The two password fields didn’t match.')
        self.assertFalse(User.objects.filter(email='jhon4@beatles.com').exists())