from django.db import models

from user.models import User


class Image(models.Model):
    image = models.ImageField('이미지', upload_to='color')

    user = models.ForeignKey(User, on_delete=models.CASCADE)