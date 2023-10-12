from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Message

User = get_user_model()
USER_DATA_TEST = dict(
    username='john123',
    email='jhon4@beatles.com',
    password='1mag1n3',
    first_name='john',
    last_name='lennon'
)


class MessageTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(
            **USER_DATA_TEST
        )
    
    def test_message_created(self):
        user = User.objects.get(username=USER_DATA_TEST["username"])
        obj = Message.objects.create(
            username=user.username,
            content="Imagine all the people. Livin' for today",
            user=user,
            room="the-70"
        )
        self.assertIsNotNone(obj)


class TestCalls(TestCase):
    login_path = '/accounts/login/?redirect_to='

    def setUp(self):
        User.objects.create_user(
            **USER_DATA_TEST
        )

    def test_call_view_deny_anonymous_homepage(self):
        url_path = "/"
        response = self.client.get(url_path, follow=True)
        self.assertRedirects(response, self.login_path + url_path)
        response = self.client.post(url_path, follow=True)
        self.assertRedirects(response, self.login_path + url_path)

    def test_call_view_load_homepage(self):
        self.client.login(username=USER_DATA_TEST["username"], password=USER_DATA_TEST["password"])
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'chat/index.html')

    def test_call_view_deny_anonymous_room(self):
        url_path = "/room/test/"
        response = self.client.get(url_path, follow=True)
        self.assertRedirects(response, self.login_path + url_path)
        response = self.client.post(url_path, follow=True)
        self.assertRedirects(response, self.login_path + url_path)

    def test_call_view_load_room(self):
        self.client.login(username=USER_DATA_TEST["username"], password=USER_DATA_TEST["password"])
        response = self.client.get('/room/test/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'chat/room.html')