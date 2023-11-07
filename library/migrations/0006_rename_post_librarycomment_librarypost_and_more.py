# Generated by Django 4.2.3 on 2023-10-15 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_alter_librarycomment_created_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='librarycomment',
            old_name='post',
            new_name='librarypost',
        ),
        migrations.AddField(
            model_name='librarypost',
            name='library_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]