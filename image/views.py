from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from image.serializers import ImageSerializer
from color.models import Color


class ImageViewSet(mixins.CreateModelMixin,
                   viewsets.GenericViewSet):
    queryset = Color.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
