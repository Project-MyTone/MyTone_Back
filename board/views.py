from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from board.models import Board
from board.serializers import (
    BoardSerializer
)


class BoardListViewSet(mixins.ListModelMixin,
                       viewsets.GenericViewSet):
    """
    보드 리스트 뷰셋
    """
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
