# Generated by Django 4.2.4 on 2024-02-02 02:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0018_alter_post_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='participant',
        ),
    ]
