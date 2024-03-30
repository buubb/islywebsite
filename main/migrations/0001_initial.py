# Generated by Django 4.2.3 on 2024-03-21 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='activity_records_count',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('years', models.IntegerField(verbose_name='누적 년도')),
                ('applicants', models.IntegerField(verbose_name='누적 지원자 수')),
                ('members', models.IntegerField(verbose_name='누적 부원 수')),
                ('projects', models.IntegerField(verbose_name='누적 프로젝트 수')),
            ],
            options={
                'verbose_name': '동아리 누적 활동 기록',
                'verbose_name_plural': 'Activity Record',
            },
        ),
        migrations.CreateModel(
            name='special_activities_tab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='제목')),
                ('content', models.TextField(max_length=250, verbose_name='내용')),
                ('image', models.ImageField(null=True, upload_to='images', verbose_name='사진')),
            ],
            options={
                'verbose_name': '특별활동 리스트',
                'verbose_name_plural': 'Special Activities',
            },
        ),
    ]
