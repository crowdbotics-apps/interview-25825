from django.test import TestCase
from django.contrib.auth import get_user_model
from home.api.models import *


class ApiAppTests(TestCase):
    def setUp(self):
        User = get_user_model()
        User.objects.create(
            username="Jonny",
            email="TestEmail@gmail.com",
            password="MySecurePassword123"
        )

    def test_create_app(self):
        User = get_user_model()
        user = User.objects.get(email="TestEmail@gmail.com")
        self.assertEqual(user.email, "TestEmail@gmail.com")
        name = "Super Cool App"
        description = "This is my super cool app for testing"
        framework = "DJ"
        # subscription
        # User = get_user_model()
        # app = App.objects.create(
        #     Name=name,
        #     description=description,
        #
        # )
