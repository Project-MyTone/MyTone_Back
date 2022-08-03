from django.urls import path

from board.views import (
    BoardListViewSet,
    BoardArticleListCreateViewSet
)


board_list = BoardListViewSet.as_view({
    'get': 'list'
})

board_article_list_create = BoardArticleListCreateViewSet.as_view({
    'get': 'list',
    'post': 'create'
})


urlpatterns = [
    path('', board_list, name='board_list'),
    path('<int:board_id>/article/', board_article_list_create, name='board_article_list_create'),
]