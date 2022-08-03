from board.models import Board


def gen_master(apps, schema_editor):
    Board(name='여름 쿨톤').save()
    Board(name='겨울 쿨톤').save()
    Board(name='가을 웜톤').save()
    Board(name='봄 웜톤').save()
