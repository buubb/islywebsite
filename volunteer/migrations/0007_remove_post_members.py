# Generated by Django 4.2.4 on 2023-12-02 20:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0006_post_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='members',
        ),
    ]
