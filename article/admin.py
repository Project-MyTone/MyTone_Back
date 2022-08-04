from django.contrib import admin

from article.models import Article, ArticleImage, ArticleLikeUser


admin.site.register(Article)
admin.site.register(ArticleImage)
admin.site.register(ArticleLikeUser)
