from django.test import TestCase

from users.models import User


class ModelsTestCase(TestCase):
    def test_user_str(self):
        userManager = User.objects.create(
            email="User@hotmail.fr",
            username="User1",
            password="pass246"
        )
        self.assertEqual(str(userManager), "User@hotmail.fr")

    def test_superuser_is_admin(self):
        superUser = User.objects.create_superuser(
            username="User2",
            email="superUser@gmail.com",
            password="pass246"
        )
        self.assertIs(superUser.is_admin, True)

    def test_user_not_admin(self):
        user = User.objects.create(
            username="User3",
            email="user@gmail.com",
            password="pass246"
        )
        self.assertIs(user.is_admin, False)

# coverage run --source"." manage.py test
