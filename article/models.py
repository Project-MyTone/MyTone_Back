from django.db import models

from board.models import Board
from user.models import User


class Article(models.Model):
    title = models.CharField('제목', max_length=150)
    content = models.TextField('내용')
    hits = models.PositiveIntegerField('조회수', default=0)

    created_at = models.DateTimeField('생성 날짜', auto_now_add=True)
    updated_at = models.DateTimeField('수정 날짜', auto_now=True)

    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article_like_user = models.ManyToManyField(User, through='article.ArticleLikeUser',
                                               related_name='article_like')

    class Meta:
        db_table = 'article'

    def __str__(self):
        return f'{self.id} - {self.title}'


class ArticleImage(models.Model):
    image = models.ImageField('이미지', upload_to='article/%Y/%m/%d')

    created_at = models.DateTimeField('생성 날짜', auto_now_add=True)

    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    class Meta:
        db_table = 'article_image'

    def __str__(self):
        return f'{self.id} // article : {self.article.title}'


class ArticleLikeUser(models.Model):
    created_at = models.DateTimeField('생성 날짜', auto_now_add=True)

    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'article_like_user'

    def __str__(self):
        return f'article : {self.article.id} / user : {self.user.id}'


