# Generated by Django 4.0.6 on 2022-08-09 04:41

from django.db import migrations, models
import django.db.models.deletion

from color.utils.gen_master_data import gen_master


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='컬러 이름')),
            ],
            options={
                'db_table': 'color',
            },
        ),
        migrations.CreateModel(
            name='Cosmetic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='화장품 이름')),
                ('image', models.CharField(max_length=255, verbose_name='이미지')),
                ('url', models.URLField(verbose_name='url')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='color.color')),
            ],
            options={
                'db_table': 'cosmetic',
            },
        ),
        migrations.RunPython(gen_master),
    ]
