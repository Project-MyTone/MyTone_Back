from rest_framework import serializers

from django.utils.translation import gettext_lazy as _

from image.models import Image
from image.personal_color_analysis import personal_color


class ImageSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Image
        fields = [
            'user',
            'image'
        ]

    # image = serializers.ImageField()
    #
    # def validate_image(self, image):
    #     if not image:
    #         raise serializers.ValidationError(
    #             _('image field not allowed empty')
    #         )
    #     return image
    #
    # def create(self, validated_data):
    #     image = validated_data['image']
    #     print(image)
    #     result = personal_color.analysis(image)
    #     return result



