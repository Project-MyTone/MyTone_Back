from django.db import transaction
from django.db.models import Q
from django.shortcuts import get_object_or_404

from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from comment.models import Comment, ReComment
from comment.serializers import (
    CommentSerializer,
    CommentCreateSerializer,
    CommentDetailUpdateDeleteSerializer,
    ReCommentSerializer,
    ReCommentCreateSerializer,
    ReCommentDetailUpdateDeleteSerializer
)
from MyTone.utils.permissions import IsOwnerOrReadOnly


class CommentListCreateViewSet(mixins.ListModelMixin,
                               mixins.CreateModelMixin,
                               viewsets.GenericViewSet):
    """
    댓글 조회, 생성
    """
    queryset = Comment.objects.all()
    permission_classes = [IsOwnerOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CommentSerializer
        else:
            return CommentCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentDetailUpdateDeleteViewSet(mixins.RetrieveModelMixin,
                                       mixins.UpdateModelMixin,
                                       mixins.DestroyModelMixin,
                                       viewsets.GenericViewSet):
    """
    댓글 상세 조회, 수정 삭제
    """
    lookup_url_kwarg = 'comment_id'
    queryset = Comment.objects.all()
    permission_classes = [IsOwnerOrReadOnly]

    def get_serializer_class(self):
        return CommentDetailUpdateDeleteSerializer

    def partial_update(self, request, *args, **kwargs):
        """
        부분 수정
        """
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)


class CommentReCommentListViewSet(mixins.ListModelMixin,
                                  viewsets.GenericViewSet):
    """
    댓글별 대댓글 목록 조회
    """
    def get_queryset(self):
        comment_id = self.kwargs['comment_id']
        return ReComment.objects \
            .filter(comment_id=comment_id) \
            .prefetch_related('user') \
            .all()

    def get_serializer_class(self):
        return ReCommentSerializer


class ReCommentListCreateViewSet(mixins.ListModelMixin,
                                 mixins.CreateModelMixin,
                                 viewsets.GenericViewSet):
    """
    대댓글 전체 조회, 생성
    """
    queryset = ReComment.objects.all()
    permission_classes = [IsOwnerOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ReCommentSerializer
        else:
            return ReCommentCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ReCommentDetailUpdateDeleteViewSet(mixins.RetrieveModelMixin,
                                         mixins.UpdateModelMixin,
                                         mixins.DestroyModelMixin,
                                         viewsets.GenericViewSet):
    """
    대댓글 상세 조회, 수정, 삭제
    """
    lookup_url_kwarg = 'recomment_id'

    queryset = ReComment.objects.all()
    serializer_class = ReCommentDetailUpdateDeleteSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def partial_update(self, request, *args, **kwargs):
        """
        부분 수정
        """
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)