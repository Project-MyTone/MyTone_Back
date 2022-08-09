from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response

from image.serializers import ImageSerializer
from color.models import Color
from image.personal_color_analysis import personal_color


class ImageViewSet(mixins.CreateModelMixin,
                   viewsets.GenericViewSet):
    queryset = Color.objects.all()
    serializer_class = ImageSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        print(serializer.data['image'])
        personal_color.analysis(serializer.data['image'])






