# Generated by Django 4.2.4 on 2023-08-27 19:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='글 제목')),
                ('contents', models.TextField(verbose_name='글 내용')),
                ('writer_dttm', models.DateTimeField(auto_now_add=True, verbose_name='글 작성일')),
                ('updata_dttm', models.DateTimeField(auto_now=True, verbose_name='마지막 수정일')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='작성자')),
            ],
            options={
                'verbose_name': '게시판',
                'verbose_name_plural': '게시판',
                'db_table': 'library',
            },
        ),
    ]