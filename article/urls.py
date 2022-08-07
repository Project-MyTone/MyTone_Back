from django.urls import path

from article.views import (
    ArticleListCreateViewSet,
    ArticleDetailUpdateDeleteViewSet,
    ArticleCommentListViewSet
)


article_list = ArticleListCreateViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

article_detail_update_delete = ArticleDetailUpdateDeleteViewSet.as_view({
    'get': 'retrieve',
    'patch': 'partial_update',
    'delete': 'destroy',
})

article_like = ArticleDetailUpdateDeleteViewSet.as_view({
    'post': 'like'
})

article_comment_list = ArticleCommentListViewSet.as_view({
    'get': 'list'
})


urlpatterns = [
    path('', article_list, name='article_list'),
    path('<int:article_id>/', article_detail_update_delete),
    path('<int:article_id>/like', article_like),
    path('<int:article_id>/comment/', article_comment_list),
]