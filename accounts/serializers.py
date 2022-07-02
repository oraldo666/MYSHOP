from djoser.serializers import UserCreateSerializer
from accounts.models import CustomUser

from djoser.serializers import TokenCreateSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.serializers import ValidationError

from rest_framework_simplejwt.views import TokenObtainPairView


class UserCreateSerializer(UserCreateSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'first_name', 'last_name')


class CustomTokenPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.first_name
        token['lname'] = user.last_name
        # ...

        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        first_name = self.user.first_name
        email = self.user.email
        id = self.user.id

        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        data["test"] = "value"
        data['first_name'] = first_name
        data["email"] = email
        data["id"] = id

        return data


class CutomObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenPairSerializer
