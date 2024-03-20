from django.db import models

class SpecialActivitiesPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title
    
class ActivityRecordsInt(models.Model):
    years = models.IntegerField()
    applicants = models.IntegerField()
    members = models.IntegerField()
    projects = models.IntegerField()

    def __str__(self):
        return self.years