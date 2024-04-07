# Generated by Django 4.2.4 on 2024-04-06 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruit', '0011_leadercontact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(max_length=20, unique=True, verbose_name='회장단 연락처')),
            ],
        ),
        migrations.DeleteModel(
            name='LeaderContact',
        ),
    ]
