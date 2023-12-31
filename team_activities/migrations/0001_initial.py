# Generated by Django 4.2.3 on 2023-10-15 06:51

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
            name='TeamActivitiesPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='제목')),
                ('content', models.TextField(verbose_name='내용')),
                ('hits', models.PositiveIntegerField(default=0, verbose_name='조회수')),
                ('registered_date', models.DateTimeField(auto_now_add=True, verbose_name='등록시간')),
                ('top_fixed', models.BooleanField(default=False, verbose_name='상단고정')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='작성자')),
            ],
            options={
                'verbose_name': 'teampost',
                'verbose_name_plural': 'teampost',
                'db_table': 'teampost',
            },
        ),
    ]
