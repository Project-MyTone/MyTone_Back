from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from django.utils.translation import gettext_lazy as _

from article.models import Article, ArticleImage
from comment.models import Comment
from user.serializers import UserSerializer
from board.serializers import BoardSerializer


class ArticleImageSerializer(serializers.ModelSerializer):
    """
    게시글에 등록할 이미지 시리얼라이저
    """
    class Meta:
        model = ArticleImage
        fields = [
            'id',
            'image',
            'created_at'
        ]


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
            'user',
        ]


class ArticleCreateSerializer(serializers.ModelSerializer):
    """
    게시글 생성
    """
    title = serializers.CharField()
    content = serializers.CharField()
    user = serializers.ReadOnlyField(source='user.id')
    images = ArticleImageSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = [
            'id',
            'title',
            'content',
            'created_at',
            'board',
            'user',
            'images'
        ]

    def create(self, validated_data):
        images_data = self.context['request'].FILES
        article = Article.objects.create(**validated_data)
        for image_data in images_data.getlist('image'):
            ArticleImage.objects.create(article=article, image=image_data)
        return article


class ArticleDetailSerializer(serializers.ModelSerializer):
    """
    게시글 상세 조회 시리얼라이저
    """
    article_like_user = serializers.SerializerMethodField(read_only=True)
    board = BoardSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    images = ArticleImageSerializer(many=True, read_only=True)

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
            'user',
            'images'
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


class ArticleImageCreateDelete(serializers.ModelSerializer):
    """
    해당 게시글의 이미지 추가
    삭제
    """
    class Meta:
        model = ArticleImage
        fields = [
            'id',
            'image',
            'article',
        ]


class ArticleCommentListSerializer(serializers.ModelSerializer):
    """
    게시글별 댓글 목록 조회
    """
    class Meta:
        model = Comment
        fields = [
            'id',
            'body',
            'reg_date',
            'update_date',
            'user',
            'article'
        ]
