from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser


class UserManager(BaseUserManager):
    def create_user(self, username, password, nickname, **extra_fields):

        if not username:
            raise ValueError("이름은 필수 항목입니다.")
        if not password:
            raise ValueError("비밀번호는 필수 항목입니다.")
        if not nickname:
            raise ValueError("닉네임은 필수 항목 입니다.")

        user = self.model(
            username=username,
            nickname=nickname
        )
        user.set_password(password)
        user.full_clean()
        user.save(using=self._db)

        return user

    def create_superuser(self, password, username, nickname, **extra_fields):

        user = self.model(
            username=username,
            nickname=nickname
        )
        user.set_password(password)
        user.full_clean()

        user.is_admin = True
        user.is_superuser = True

        user.save(using=self._db)

        return


class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = 'M', '남성'
        FEMALE = 'F', '여성'

    first_name = None
    last_name = None
    date_joined = None
    name = None

    nickname = models.CharField('닉네임', max_length=50)
    gender = models.CharField('성별', max_length=1, blank=True, choices=GenderChoices.choices)
    color = models.CharField('컬러', max_length=20, blank=True)

    created_at = models.DateTimeField('생성 날짜', auto_now_add=True)
    update_date = models.DateTimeField('수정 날짜', auto_now=True)

    class Meta:
        db_table = 'user'

    def __str__(self):
        return f'{self.id}, {self.username}, {self.nickname}'