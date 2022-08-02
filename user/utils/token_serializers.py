from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    토큰 커스텀
    """
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['nickname'] = user.name
        token['gender'] = user.gender
        token['is_admin'] = user.is_staff
        token['is_active'] = user.is_active

        return token


class APIRefreshTokenSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    pass