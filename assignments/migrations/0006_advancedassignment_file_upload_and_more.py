# Generated by Django 4.2.3 on 2023-09-26 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("assignments", "0005_basicassignment_file_upload"),
    ]

    operations = [
        migrations.AddField(
            model_name="advancedassignment",
            name="file_upload",
            field=models.FileField(
                blank=True, default="default_value.pdf", null=True, upload_to="uploads/"
            ),
        ),
        migrations.AlterField(
            model_name="basicassignment",
            name="file_upload",
            field=models.FileField(
                blank=True, default="default_value.pdf", null=True, upload_to="uploads/"
            ),
        ),
    ]
