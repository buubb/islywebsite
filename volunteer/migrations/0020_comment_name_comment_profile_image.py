# Generated by Django 5.0.4 on 2024-05-05 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0019_remove_post_participant'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(default='', max_length=10, verbose_name='이름'),
        ),
        migrations.AddField(
            model_name='comment',
            name='profile_image',
            field=models.ImageField(null=True, upload_to='comment/profile', verbose_name='프로필 이미지'),
        ),
    ]