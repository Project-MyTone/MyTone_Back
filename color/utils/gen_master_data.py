from color.models import Color


def gen_master(apps, schema_editor):
    Color(name='여름 쿨톤').save()
    Color(name='겨울 쿨톤').save()
    Color(name='가을 웜톤').save()
    Color(name='봄 웜톤').save()
