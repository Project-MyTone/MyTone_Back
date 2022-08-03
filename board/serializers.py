from rest_framework import serializers

from board.models import Board


class BoardSerializer(serializers.ModelSerializer):
    """
    보드 시리얼라이저
    """
    class Meta:
        model = Board
        fields = [
            'id',
            'name',
            'created_at'
        ]