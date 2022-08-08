from django.urls import path

from comment.views import (
    CommentListCreateViewSet,
    CommentDetailUpdateDeleteViewSet,
    ReCommentListCreateViewSet,
    CommentReCommentListViewSet,
    ReCommentDetailUpdateDeleteViewSet
)


comment_list_create = CommentListCreateViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
comment_detail_update_delete = CommentDetailUpdateDeleteViewSet.as_view({
    'get': 'retrieve',
    'patch': 'partial_update',
    'delete': 'destroy'
})

comment_recomment_list = CommentReCommentListViewSet.as_view({
    'get': 'list'
})

recomment_list_create = ReCommentListCreateViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

recomment_detail_update_delete = ReCommentDetailUpdateDeleteViewSet.as_view({
    'get': 'retrieve',
    'patch': 'partial_update',
    'delete': 'destroy'
})


urlpatterns = [
    path('', comment_list_create),
    path('<int:comment_id>/', comment_detail_update_delete),
    path('<int:comment_id>/recomment/', comment_recomment_list),
    path('recomment/', recomment_list_create),
    path('recomment/<int:recomment_id>/', recomment_detail_update_delete),
]