from django.db import models

from user.models import User
from article.models import Article


class Comment(models.Model):
    body = models.TextField('댓글 내용')

    reg_date = models.DateTimeField('생성 날짜', auto_now_add=True)
    update_date = models.DateTimeField('수정 날짜', auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    class Meta:
        db_table = 'comment'

    def __str__(self):
        return f'{self.id} / article : {self.article} / user : {self.user}'


class ReComment(models.Model):
    body = models.TextField('대댓글 내용')

    reg_date = models.DateTimeField('생성 날짜', auto_now_add=True)
    update_date = models.DateTimeField('수정 날짜', auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

    class Meta:
        db_table = 'recomment'

    def __str__(self):
        return f'{self.id} / comment : {self.comment} / user : {self.user}'

