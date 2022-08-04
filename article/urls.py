from django.urls import path

from article.views import (
    ArticleListCreateViewSet,
    ArticleDetailUpdateDeleteViewSet
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


urlpatterns = [
    path('', article_list, name='article_list'),
    path('<int:article_id>/', article_detail_update_delete),
    path('<int:article_id>/like', article_like),
]