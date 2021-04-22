from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from home.api.v1.serializers import (
    SignupSerializer,
    CustomTextSerializer,
    HomePageSerializer,
    UserSerializer,
    AppsSerializer,
    AppsOneSerializer,
    PlansSerializer,
    SubscriptionSerializer,
)
from home.models import CustomText, HomePage
from home.api.models import App, Plan, Subscription


class SignupViewSet(ModelViewSet):
    serializer_class = SignupSerializer
    http_method_names = ["post"]


class LoginViewSet(ViewSet):
    """Based on rest_framework.authtoken.views.ObtainAuthToken"""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        user_serializer = UserSerializer(user)
        return Response({"token": token.key, "user": user_serializer.data})


class CustomTextViewSet(ModelViewSet):
    serializer_class = CustomTextSerializer
    queryset = CustomText.objects.all()
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = [IsAdminUser]
    http_method_names = ["get", "put", "patch"]


class HomePageViewSet(ModelViewSet):
    serializer_class = HomePageSerializer
    queryset = HomePage.objects.all()
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = [IsAdminUser]
    http_method_names = ["get", "put", "patch"]


class AppsAllViewSet(ModelViewSet):
    serializer_class = AppsSerializer
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return App.objects.filter(User=self.request.user)

    http_method_names = ["get", "post"]


class AppsViewOneSet(ModelViewSet):
    serializer_class = AppsOneSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        return App.objects.filter(User=self.request.user)

    http_method_names = ["get", "put", "patch", "delete"]


class PlansViewSet(ModelViewSet):
    serializer_class = PlansSerializer
    lookup_field = 'id'
    queryset = Plan.objects.all()

    http_method_names = ["get"]


class SubscriptionViewSet(ModelViewSet):
    serializer_class = SubscriptionSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Subscription.objects.filter(User=self.request.user)

    http_method_names = ["get", "post", "put", "patch"]

