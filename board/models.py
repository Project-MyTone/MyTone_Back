from django.db import models


class Board(models.Model):
    name = models.CharField('보드 이름', max_length=20)
    created_at = models.DateTimeField('생성 날짜', auto_now_add=True)

    class Meta:
        db_table = 'board'

    def __str__(self):
        return self.name
