from django.urls import path, include
from rest_framework.routers import DefaultRouter

from home.api.v1.viewsets import (
    SignupViewSet,
    LoginViewSet,
    HomePageViewSet,
    CustomTextViewSet,
    AppsAllViewSet,
    AppsViewOneSet,
)

router = DefaultRouter()
router.register("signup", SignupViewSet, basename="signup")
router.register("login", LoginViewSet, basename="login")
router.register("customtext", CustomTextViewSet)
router.register("homepage", HomePageViewSet)
router.register("apps", AppsAllViewSet, basename="apps")
router.register("apps_id", AppsViewOneSet, basename="apps_id")

urlpatterns = [
    path("", include(router.urls)),
]
