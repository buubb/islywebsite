# Generated by Django 4.2.4 on 2024-01-06 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0015_alter_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='year',
            field=models.PositiveIntegerField(default=2020, null=True, verbose_name='연도'),
        ),
    ]
