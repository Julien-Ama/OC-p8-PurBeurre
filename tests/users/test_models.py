from django.test import TestCase

from users.models import User


class ModelsTestCase(TestCase):
    def test_user_str(self):


    def test_superuser_is_admin(self):


    def test_user_not_admin(self):



# coverage run --source"." manage.py test