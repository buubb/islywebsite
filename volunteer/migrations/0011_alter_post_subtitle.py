# Generated by Django 4.2.4 on 2023-12-02 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0010_post_subtitle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='subtitle',
            field=models.CharField(default='', max_length=200, null=True, verbose_name='소제목'),
        ),
    ]
