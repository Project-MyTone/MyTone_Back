from rest_framework import serializers

from board.models import Board
from article.models import (
    Article,
    ArticleImage,
    ArticleLikeUser
)
from user.serializers import UserSerializer


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


class BoardArticleListSerializer(serializers.ModelSerializer):
    """
    아티클 리스트 조회
    시리얼라이저
    """
    board = BoardSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    article_like_user = serializers.SerializerMethodField(read_only=True)

    def get_article_like_user(self, obj):
        return obj.article_like_user.count()

    class Meta:
        model = Article
        fields = [
            'id',
            'title',
            'hits',
            'board',
            'user',
            'article_like_user',
        ]


class BoardArticleCreateSerializer(serializers.ModelSerializer):
    """
    아티클 생성 시리얼라이저
    """
    title = serializers.CharField()
    content = serializers.CharField()
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Article
        fields = [
            'id',
            'title',
            'content',
            'user',
            'created_at'
        ]

