from django.urls import path, include

from accounts.serializers import CutomObtainPairView


from djoser.views import UserViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .serializers import CustomTokenPairSerializer

app_name = "authenticate"

urlpatterns = [
    path('register/',
         UserViewSet.as_view({'post': 'create'}, name="register")),

    #   path("login/", TokenObtainPairView.as_view(), name="login"),
    #   This url is a not customized jwt token -- The next url is

    path("login/", CutomObtainPairView.as_view(), name="login"),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path("resend-activation/",
         UserViewSet.as_view({"post": "resend_activation"}), name="resend_activation"),
    path("activate/<str:uid>/<str:token>/",
         UserViewSet.as_view({"post": "activation"}), name="activation"),

    path("reset-password/",
         UserViewSet.as_view({"post": "reset_password"}), name="reset_password"),
    path("password/reset/confirm/<str:uid>/<str:token>/", UserViewSet.as_view(
        {"post": "reset_password_confirm"}), name="reset_password_confirm"),
]
