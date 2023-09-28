from django.conf import settings
from django.db import models

class LibraryPost(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,  null=True)

    def __str__(self):
        return self.subject