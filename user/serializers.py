from rest_framework import serializers

from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _

from user.models import User
from user.utils.valid_password import validate_password12
from user.utils.token_serializers import MyTokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):
    """
    유저 시리얼라이저
    """
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'nickname',
            'gender',
            'color',
            'created_at'
        ]


class UserUpdateDeleteSerializer(serializers.ModelSerializer):
    """
    유저 수정, 삭제 시리얼라이저
    """
    class Meta:
        model = User
        fields = [
            'nickname',
            'gender'
        ]


class UserCreateSerializer(serializers.Serializer):
    """
    회원가입 시리얼라이저
    """
    username = serializers.CharField(max_length=100, write_only=True)
    password1 = serializers.CharField(max_length=100, write_only=True)
    password2 = serializers.CharField(max_length=100, write_only=True)
    nickname = serializers.CharField(max_length=100, write_only=True)
    gender = serializers.ChoiceField(User.GenderChoices)

    def validate_username(self, username):
        """
        유저 아이디 유효성 검사
        """
        # case : username 빈 칸인 경우
        if not username:
            raise serializers.ValidationError(
                _('username field not allowed empty')
            )

        get_user = User.objects.filter(username__iexact=username)

        # case : 이미 가입된 username인 경우
        if get_user.count() > 0:
            raise serializers.ValidationError(
                _('username is already registered')
            )
        return username

    def validate(self, data):
        """
        검증 데이터
        """
        data['username'] = self.validate_username(data['username'])
        data['password1'] = validate_password12(data['password1'], data['password2'])

        return data

    def create(self, validate_data):
        """
        유저 생성
        """
        user = User.objects.create_user(
            username=validate_data['username'],
            password=validate_data['password1'],
            nickname=validate_data['nickname'],
            gender=validate_data['gender'],
        )
        return user


class UserLoginSerializer(serializers.ModelSerializer):
    """
    로그인 시리얼라이저
    """
    username = serializers.CharField(max_length=100, write_only=True)
    password = serializers.CharField(max_length=100, write_only=True)

    class Meta:
        model = User
        fields = [
            'username',
            'password'
        ]

    def validate_username(self, username):
        if not username:
            raise serializers.ValidationError(
                _('username field not allowed empty')
            )

        return username

    def validate_password(self, password):
        if not password:
            raise serializers.ValidationError(
                _('password field not allowed empty')
            )

        return password

    def validate(self, data):
        """
        유효성 검사
        """
        username = self.validate_username(data['username'])
        password = self.validate_password(data['password'])

        # case : username이 존재하는 경우
        if User.objects.filter(username=username).exists():
            get_user = User.objects.get(username=username)

            # case : password가 다른 경우
            if not get_user.check_password(password):
                raise serializers.ValidationError(
                    _('Check Your Password')
                )
        else:
            raise serializers.ValidationError(
                _('User does not exist')
            )

        user = authenticate(username=username, password=password)
        token = MyTokenObtainPairSerializer.get_token(user)

        data = {
            'user': user.id,
            'access_token': str(token.access_token),
            'refresh_token': str(token),
        }

        return data




