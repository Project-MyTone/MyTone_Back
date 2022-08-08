from rest_framework import serializers

from comment.models import Comment, ReComment


class CommentSerializer(serializers.ModelSerializer):
    """
    댓글 목록 조회 시리얼라이저
    """
    class Meta:
        model = Comment
        fields = [
            'id',
            'body',
            'created_at',
            'updated_at',
            'user',
            'article'
        ]


class CommentCreateSerializer(serializers.ModelSerializer):
    """
    댓글 생성 시리얼라이저
    """
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Comment
        fields = [
            'id',
            'body',
            'created_at',
            'updated_at',
            'user',
            'article'
        ]


class CommentDetailUpdateDeleteSerializer(serializers.ModelSerializer):
    """
    댓글 상세 조회
    수정
    삭제
    시리얼라이저
    """
    class Meta:
        model = Comment
        fields = [
            'id',
            'body',
            'created_at',
            'updated_at',
            'user',
            'article'
        ]
        read_only_fields = [
            'article',
            'user'
        ]


class ReCommentSerializer(serializers.ModelSerializer):
    """
    대댓글 시리얼라이저
    """
    class Meta:
        model = ReComment
        fields = [
            'id',
            'body',
            'created_at',
            'updated_at',
            'user',
            'comment'
        ]


class ReCommentCreateSerializer(serializers.ModelSerializer):
    """
    대댓글 생성 시리얼라이저
    """
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = ReComment
        fields = [
            'id',
            'body',
            'created_at',
            'updated_at',
            'user',
            'comment'
        ]


class ReCommentDetailUpdateDeleteSerializer(serializers.ModelSerializer):
    """
    대댓글 상세 조회
    수정
    삭제
    """
    class Meta:
        model = ReComment
        fields = [
            'id',
            'body',
            'created_at',
            'updated_at',
            'user',
            'comment'
        ]
        read_only_fields = [
            'user',
            'comment'
        ]