# Generated by Django 4.2.4 on 2023-12-02 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0009_post_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='subtitle',
            field=models.CharField(default='', max_length=100, null=True, verbose_name='소제목'),
        ),
    ]
