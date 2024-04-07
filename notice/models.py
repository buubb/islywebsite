from django.db import models


class AttendanceLink(models.Model):
    link = models.URLField()

    def __str__(self):
        return self.link


class SubmissionLink(models.Model):
    link = models.URLField()

    def __str__(self):
        return self.link


class RentalLink(models.Model):
    link = models.URLField()

    def __str__(self):
        return self.link