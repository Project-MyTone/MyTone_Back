from django.urls import path

from board.views import (
    BoardListViewSet
)


board_list = BoardListViewSet.as_view({
    'get': 'list'
})


urlpatterns = [
    path('', board_list, name='board_list'),
]