# Generated by Django 4.2.4 on 2023-09-07 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0002_post_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='members',
            field=models.CharField(default='', max_length=100, null=True, verbose_name='팀원'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default='', max_length=100, null=True, verbose_name='포스트 제목'),
        ),
    ]
