# models.py
from django.db import models
from django.core.exceptions import ValidationError
import re


class Recruitment(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    application_link = models.URLField()

    def __str__(self):
        return f"Recruitment from {self.start_date} to {self.end_date}"

    def clean(self):
        if self.end_date < self.start_date:
            raise ValidationError("End date must be after start date.")

        if Announcement.objects.filter(start_date__lte=self.end_date, end_date__gte=self.start_date).exists():
            raise ValidationError("There is an overlapping period with the announcement period.")


class Announcement(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"Announcement from {self.start_date} to {self.end_date}"

    def clean(self):
        if self.end_date < self.start_date:
            raise ValidationError("End date must be after start date.")

        if Recruitment.objects.filter(start_date__lte=self.end_date, end_date__gte=self.start_date).exists():
            raise ValidationError("There is an overlapping period with the recruitment period.")


class Applicant(models.Model):
    name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20, unique=True)
    phone_number = models.CharField(max_length=20, unique=True)
    is_passed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def clean(self):
        self.phone_number = re.sub(r"\D", "", self.phone_number)

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)