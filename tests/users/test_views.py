from django.test import TestCase, Client
from django.urls import reverse

from users.models import User
# from users.views import *


class TestUsersViews(TestCase):
    def setUp(self):
        self.client = Client()
        # self.form = UserRegisterForm()
        self.user = User.objects.create_user(
            username="user1",
            email="user1@gmail.com",
            password="pass246",
        )
        self.account_url = reverse("account")
        self.register_url = reverse("register")

    def test_registration_success(self):
        form = {
            "email": "user1@gmail.com",
            "username": "user1",
            "password1": "pass246",
            "password2": "pass246"
        }
        self.client.post(self.register_url, form)
        self.assertEqual(User.objects.count(), 1)
        self.client.force_login(self.user)

    def test_account_page(self):
        self.client.force_login(self.user)
        response = self.client.get(self.account_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "account.html")
