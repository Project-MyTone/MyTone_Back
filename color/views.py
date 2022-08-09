from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from color.serializers import (
    ColorSerializer,
    CosmeticSerializer
)
from color.models import Color, Cosmetic


class ColorListDetailViewSet(mixins.ListModelMixin,
                             mixins.RetrieveModelMixin,
                             viewsets.GenericViewSet):
    """
    컬러 조회
    """
    lookup_url_kwarg = 'color_id'

    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class CosmeticListDetailViewSet(mixins.ListModelMixin,
                                viewsets.GenericViewSet):
    """
    컬러별 화장품 조회
    """
    serializer_class = CosmeticSerializer

    def get_queryset(self):
        color_id = self.kwargs['color_id']
        return Cosmetic.objects \
            .filter(color_id=color_id) \
            .all()

