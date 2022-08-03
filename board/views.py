from django.db import transaction

from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from board.models import Board
from article.models import Article
from board.serializers import (
    BoardSerializer,
    BoardArticleListSerializer,
    BoardArticleCreateSerializer
)


class BoardListViewSet(mixins.ListModelMixin,
                       viewsets.GenericViewSet):
    """
    보드 리스트 뷰셋
    """
    queryset = Board.objects.all()
    serializer_class = BoardSerializer


class BoardArticleListCreateViewSet(mixins.ListModelMixin,
                                    mixins.CreateModelMixin,
                                    viewsets.GenericViewSet):
    """
    보드 아티클 리스트 조회
    보드 아티클 생성
    뷰셋
    """
    def get_queryset(self):
        board_id = self.kwargs['board_id']

        return Article.objects \
            .filter(board_id=board_id) \
            .prefetch_related('board') \
            .all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BoardArticleListSerializer
        else:
            return BoardArticleCreateSerializer

    # @transaction.atomic()
    # def create(self, request, *args, **kwargs):
    #     return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user,
            board_id=self.kwargs['board_id']
        )


