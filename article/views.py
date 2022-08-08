import socket

from django.db import transaction
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.core.cache import cache

from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from article.models import Article
from comment.models import Comment
from article.serializers import (
    ArticleSerializer,
    ArticleDetailSerializer,
    ArticleCreateSerializer,
    ArticleUpdateDeleteSerializer,
    ArticleCommentListSerializer
)
from MyTone.utils.permissions import IsOwnerOrReadOnly
from MyTone.utils.pagination import ArticlePageNumberPagination


class ArticleListCreateViewSet(mixins.ListModelMixin,
                               mixins.CreateModelMixin,
                               viewsets.GenericViewSet):
    """
    아티클 리스트 조회
    """
    queryset = Article.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
    pagination_class = ArticlePageNumberPagination

    def get_queryset(self):
        if self.request.method == 'GET':
            search = self.request.GET.get('search', '')

            condition = Q()
            if search:
                condition.add(
                    Q(title__icontains=search),
                    Q.OR
                )

            return Article.objects.filter(condition)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ArticleSerializer
        else:
            return ArticleCreateSerializer

    @transaction.atomic()
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ArticleDetailUpdateDeleteViewSet(mixins.RetrieveModelMixin,
                                       mixins.UpdateModelMixin,
                                       mixins.DestroyModelMixin,
                                       viewsets.GenericViewSet):

    """
    게시글 상세 조회
    수정
    삭제
    """
    lookup_url_kwarg = 'article_id'

    queryset = Article.objects.all()
    permission_classes = [IsOwnerOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ArticleDetailSerializer
        else:
            return ArticleUpdateDeleteSerializer

    def retrieve(self, request, *args, **kwargs):
        pk = self.kwargs['article_id']
        article = get_object_or_404(Article, pk=pk)
        expire_time = 600

        user = self.request.user.id
        # 인가되지 않은 사용자 접근
        if user is None:
            user = socket.gethostbyname(socket.gethostname())

        # 캐싱을 이용해서 조회수 기능 구현
        cache_value = cache.get(f'user-{user}', '_')
        response = Response(status=status.HTTP_200_OK)

        # 인가된 사용자의 조회수 증가
        if f'_{pk}_' not in cache_value:
            cache_value += f'{pk}_'
            cache.set(f'user-{user}', cache_value, expire_time)
            article.hits += 1
            article.save()

        instance = self.get_object()
        serializer = self.get_serializer(instance)
        response.data = serializer.data
        return response




    def partial_update(self, request, *args, **kwargs):
        """
        부분 수정
        """
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    @action(detail=True, methods=['post'])
    def like(self, request, *args, **kwargs):
        """
        좋아요 기능
        """
        pk = kwargs['article_id']
        user = request.user
        article = get_object_or_404(Article, pk=pk)

        # 좋아요 취소
        if article.article_like_user.filter(pk=user.id).exists():
            article.article_like_user.remove(user.id)
        # 좋아요 추가
        else:
            article.article_like_user.add(user.id)

        return Response(status=status.HTTP_200_OK)


class ArticleCommentListViewSet(mixins.ListModelMixin,
                                viewsets.GenericViewSet):
    """
    게시글별 댓글 목록 조회
    """
    pagination_class = ArticlePageNumberPagination

    def get_queryset(self):
        article_id = self.kwargs['article_id']
        return Comment.objects \
            .filter(article_id=article_id) \
            .prefetch_related('user') \
            .prefetch_related('article') \
            .all()

    def get_serializer_class(self):
        return ArticleCommentListSerializer





