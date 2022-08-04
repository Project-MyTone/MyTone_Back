from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from django.utils.translation import gettext_lazy as _

from article.models import Article
from user.serializers import UserSerializer
from board.serializers import BoardSerializer


class ArticleSerializer(serializers.ModelSerializer):
    """
    게시글 시리얼라이저
    """
    user = serializers.SerializerMethodField(read_only=True)

    def get_user(self, obj):
        return obj.user.nickname

    class Meta:
        model = Article
        fields = [
            'id',
            'title',
            'hits',
            'created_at',
            'board',
            'user'
        ]


class ArticleCreateSerializer(serializers.ModelSerializer):
    """
    게시글 생성
    """
    title = serializers.CharField()
    content = serializers.CharField()
    user = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = Article
        fields = [
            'id',
            'title',
            'content',
            'created_at',
            'board',
            'user'
        ]


class ArticleDetailSerializer(serializers.ModelSerializer):
    """
    게시글 상세 조회 시리얼라이저
    """
    article_like_user = serializers.SerializerMethodField(read_only=True)
    board = BoardSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    def get_article_like_user(self, obj):
        return obj.article_like_user.count()

    class Meta:
        model = Article
        fields = [
            'id',
            'title',
            'content',
            'hits',
            'created_at',
            'updated_at',
            'article_like_user',
            'board',
            'user'
        ]


class ArticleUpdateDeleteSerializer(serializers.ModelSerializer):
    """
    게시글 수정
    게시글 삭제
    """
    class Meta:
        model = Article
        fields = [
            'title',
            'content',
            'board',
        ]
