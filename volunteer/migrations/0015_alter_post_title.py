# Generated by Django 4.2.4 on 2024-01-06 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0014_post_generation_alter_post_title_alter_post_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default='', max_length=50, null=True, verbose_name='포스트 제목'),
        ),
    ]
