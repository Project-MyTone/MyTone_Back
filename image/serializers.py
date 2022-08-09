from rest_framework import serializers

from django.utils.translation import gettext_lazy as _

from image.models import Image
from image.personal_color_analysis import personal_color


class ImageSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    personal = serializers.SerializerMethodField('get_personal')
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Image
        fields = [
            'user',
            'image',
            'personal'
        ]

    def get_personal(self, obj):
        request = self.context.get("request")
        get_image = request.build_absolute_uri(obj.image.url)
        return personal_color.analysis(get_image)

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



