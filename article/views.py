from django.db import transaction
from django.db.models import Q
from django.shortcuts import get_object_or_404

from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from article.models import Article
from article.serializers import (
    ArticleSerializer,
    ArticleDetailSerializer,
    ArticleCreateSerializer,
    ArticleUpdateDeleteSerializer
)


class ArticleListCreateViewSet(mixins.ListModelMixin,
                               mixins.CreateModelMixin,
                               viewsets.GenericViewSet):
    """
    아티클 리스트 조회
    """
    queryset = Article.objects.all()

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

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ArticleDetailSerializer
        else:
            return ArticleUpdateDeleteSerializer

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
        print(article.article_like_user)

        # 좋아요 취소
        if article.article_like_user.filter(pk=user.id).exists():
            article.article_like_user.remove(user.id)
        # 좋아요 추가
        else:
            article.article_like_user.add(user.id)

        return Response(status=status.HTTP_200_OK)




