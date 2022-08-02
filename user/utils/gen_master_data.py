from user.models import User


def gen_master(apps, schema_editor):
    """
    유저 더미데이터
    """

    User.objects.create_superuser(
        username='admin',
        password='admin',
        nickname='관리자',
        gender=User.GenderChoices.MALE
    )

    for i in range(2, 4):
        username = f'user{i}'
        password = f'user{i}'
        nickname = f'이름{i}'
        gender = User.GenderChoices.FEMALE

        User.objects.create_user(
            username=username,
            password=password,
            nickname=nickname,
            gender=gender
        )