from rest_framework import serializers

from color.models import Color, Cosmetic


class ColorSerializer(serializers.ModelSerializer):
    """
    컬러 시리얼라이저
    """
    class Meta:
        model = Color
        fields = [
            'id',
            'name'
        ]


class CosmeticSerializer(serializers.ModelSerializer):
    """
    화장품 시리얼라이저
    """
    class Meta:
        model = Cosmetic
        fields = [
            'id',
            'name',
            'image',
            'url',
            'color'
        ]
