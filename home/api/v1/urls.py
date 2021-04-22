from django.urls import path, include
from rest_framework.routers import DefaultRouter

from home.api.v1.viewsets import (
    SignupViewSet,
    LoginViewSet,
    HomePageViewSet,
    CustomTextViewSet,
    AppsAllViewSet,
    AppsViewOneSet,
    PlansViewSet,
)

router = DefaultRouter()
router.register("signup", SignupViewSet, basename="signup")
router.register("login", LoginViewSet, basename="login")
router.register("customtext", CustomTextViewSet)
router.register("homepage", HomePageViewSet)
router.register("apps", AppsAllViewSet, basename="apps")
# TODO change url path to match docs
router.register("apps_id", AppsViewOneSet, basename="apps_id")
router.register("plans", PlansViewSet, basename="plans")

urlpatterns = [
    path("", include(router.urls)),
]
