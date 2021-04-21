from django.db import models
from django.conf import settings
import datetime


class App(models.Model):
    """
    Maybe a foreign key pointing to a an AppType model would be better.
    This would allow more types to be added through the Django Admin rather than hard coding them in.
    Same with the frameworks
    """
    APP_TYPES = (
        ("Web", "Web"),
        ("Mobile", "Mobile")
    )
    APP_FRAMEWORKS = (
        ("DJ", "Django"),
        ("RN", "React Native")
    )
    name = models.CharField(name="Title", max_length=50, null=True, blank=True)
    description = models.TextField(name='Description', null=True, blank=True)
    type = models.CharField(name="Type", max_length=50, choices=APP_TYPES, default="Web", null=True, blank=True)
    framework = models.CharField(name="Framework", max_length=50, choices=APP_FRAMEWORKS, default="DJ", null=True, blank=True)
    screenshot = models.ImageField(name="Screenshot", upload_to="App_Screenshots", null=True, blank=True)
    subscription = models.ForeignKey("Subscription", name="Subscription", on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, name="User", on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(name="Created at", auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(name="Updated at", auto_now=True, null=True, blank=True)


class Subscription(models.Model):
    pass
