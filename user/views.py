from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from user.models import User
from user.serializers import (
    UserSerializer,
    UserUpdateDeleteSerializer,
    UserCreateSerializer,
    UserLoginSerializer
)


class UserCreateViewSet(viewsets.GenericViewSet):
    """
    회원가입 뷰셋
    """
    queryset = User.objects.all()

    def get_serializer_class(self):
        return UserCreateSerializer

    @action(detail=False, methods=['post'])
    def register(self, request):
        """
        회원가입 로직
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {
                    'message': '회원가입이 되었습니다.'
                }, status=status.HTTP_200_OK
            )
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )


class UserLoginViewSet(viewsets.GenericViewSet):
    """
    로그인 뷰셋
    """
    queryset = User.objects.all()

    def get_serializer_class(self):
        return UserLoginSerializer

    @action(detail=False, methods=['post'])
    def login(self, request):
        """
        로그인 로직
        """
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            user = request.data.get('username')
            token = serializer.validated_data
            return Response(
                {
                    'message': f'로그인 되었습니다. 반갑습니다 {user}님',
                    'token': token
                }, status=status.HTTP_200_OK
            )
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )


class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    """
    유저 상서 조회
    수정
    삭제
    뷰셋
    """
    lookup_url_kwarg = 'user_id'

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserSerializer
        else:
            return UserUpdateDeleteSerializer

    def partial_update(self, request, *args, **kwargs):
        """
        부분 수정 로직
        """
        kwargs['partial'] = True

        return self.update(request, *args, **kwargs)
