# Generated by Django 4.2.10 on 2024-04-01 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recruit", "0005_applicant"),
    ]

    operations = [
        migrations.AlterField(
            model_name="applicant",
            name="phone_number",
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name="applicant",
            name="student_id",
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
