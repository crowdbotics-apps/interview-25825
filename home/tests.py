from django.test import TestCase
from django.contrib.auth import get_user_model
from home.api.models import *


class ApiAppTests(TestCase):
    def setUp(self):
        User = get_user_model()
        user = User.objects.create(
            username="Jonny",
            email="TestEmail@gmail.com",
            password="MySecurePassword123"
        )
        plan = Plan.objects.create(
            name="Basic",
            description="Basic plan",
            price=0
        )
        Subscription.objects.create(
            user=user,
            plan=plan
        )

    def test_create_app(self):
        User = get_user_model()
        user = User.objects.get(email="TestEmail@gmail.com")
        name = "Super Cool App"
        description = "This is my super cool app for testing"
        framework = "DJ"
        subscription = Subscription.objects.get(name="Basic")

        app = App.objects.create(
            name=name,
            description=description,
            user=user,
            framework=framework,
            subscription=subscription,
        )
        self.assertEqual(app.name, name)
        self.assertEqual(app.description, description)
        self.assertEqual(app.framework, framework)
        self.assertEqual(app.subscription, subscription)


class ApiPlanTests(TestCase):

    def test_create_plan(self):

        name = "Basic Plan"
        description = "This is our basic plan"
        price = 0

        plan = Plan.objects.create(
            name=name,
            description=description,
            price=price
        )
        self.assertEqual(plan.name, name)
        self.assertEqual(plan.description, description)
        self.assertEqual(plan.price, price)


class ApiPlanSubscription(TestCase):
    def setUp(self):
        User = get_user_model()
        user = User.objects.create(
            username="Jonny",
            email="TestEmail@gmail.com",
            password="MySecurePassword123"
        )
        plan = Plan.objects.create(
            name="Basic",
            description="Basic plan",
            price=0
        )

    def test_create_subscription(self):
        User = get_user_model()
        user = User.objects.get(email="TestEmail@gmail.com")
        plan = Plan.objects.get(name="Basic")
        sub = Subscription.objects.create(
            user=user,
            plan=plan,
        )

        self.assertEqual(sub.user, user)
        self.assertEqual(sub.plan, plan)
        self.assertTrue(sub.active)