from django.urls import path

from user.views import (
    UserViewSet,
    UserCreateViewSet,
    UserLoginViewSet
)

app_name = 'user'

user_detail = UserViewSet.as_view({
    'get': 'retrieve',
    'patch': 'partial_update',
    'delete': 'destroy'
})

user_login = UserLoginViewSet.as_view({
    'post': 'login'
})

user_create = UserCreateViewSet.as_view({
    'post': 'register'
})


urlpatterns = [
    path('<int:user_id>/', user_detail, name='user_detail'),
    path('login/', user_login, name='user_login'),
    path('register/', user_create, name='user_create')
]