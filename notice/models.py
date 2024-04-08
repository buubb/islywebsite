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


class Hashtag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Lecture(models.Model):
    title = models.CharField(max_length=100)
    link = models.URLField()
    hashtags = models.ManyToManyField(Hashtag)
    thumbnail = models.ImageField(upload_to="lecture")

    def __str__(self):
        return self.title