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
    name = models.CharField(verbose_name="Name", max_length=50, null=True, blank=True)
    description = models.TextField(verbose_name='Description', null=True, blank=True)
    type = models.CharField(verbose_name="Type", max_length=50, choices=APP_TYPES, default="Web", null=True, blank=True)
    framework = models.CharField(verbose_name="Framework", max_length=50, choices=APP_FRAMEWORKS, default="DJ", null=True, blank=True)
    screenshot = models.ImageField(verbose_name="Screenshot", upload_to="App_Screenshots", null=True, blank=True)
    subscription = models.ForeignKey("Subscription", verbose_name="Subscription", on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="User", on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(verbose_name="Created at", auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(verbose_name="Updated at", auto_now=True, null=True, blank=True)

    def __str__(self):
        return str(self.name)


class Plan(models.Model):
    name = models.CharField(verbose_name="Name", max_length=20, null=True, blank=True)
    description = models.TextField(verbose_name='Description', null=True, blank=True)
    price = models.IntegerField(verbose_name=0, null=True)
    created_at = models.DateTimeField(verbose_name="Created at", auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(verbose_name="Updated at", auto_now=True, null=True, blank=True)

    def __str__(self):
        return str(self.name)


class Subscription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="User", on_delete=models.CASCADE, null=True, blank=True)
    plan = models.ForeignKey("Plan", verbose_name="Plan", on_delete=models.CASCADE, null=True, blank=True)
    active = models.BooleanField(verbose_name="Active", default=True)

    def __str__(self):
        return "{}-{}".format(self.plan.name, self.active)

