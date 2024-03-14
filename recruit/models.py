# models.py
from django.db import models

class Recruitment(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    application_link = models.URLField()

    def __str__(self):
        return f"Recruitment from {self.start_date} to {self.end_date}"
