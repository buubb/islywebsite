# Generated by Django 4.2.4 on 2024-04-07 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0003_hashtag_rental'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Rental',
            new_name='Lecture',
        ),
    ]
