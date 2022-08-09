from django.db import models


class Color(models.Model):
    name = models.CharField('컬러 이름', max_length=100)

    class Meta:
        db_table = 'color'

    def __str__(self):
        return self.name


class Cosmetic(models.Model):
    name = models.CharField('화장품 이름', max_length=200)
    image = models.CharField('이미지', max_length=255)
    url = models.URLField('url')

    color = models.ForeignKey(Color, on_delete=models.CASCADE)

    class Meta:
        db_table = 'cosmetic'

    def __str__(self):
        return f'{self.color.name} / {self.id}'


