# Generated by Django 4.2.4 on 2024-04-03 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruit', '0009_orientation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expire_after', models.DateField()),
                ('invite_link', models.URLField()),
            ],
        ),
    ]
