from django.conf import settings
from django.db import models

class LibraryPost(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,  null=True)
    modify_date = models.DateTimeField(null=True, blank=True)
    library_count = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.subject
    

class LibraryComment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,  null=True)
    content = models.TextField()
    modify_date = models.DateTimeField(null=True, blank=True)
    librarypost = models.ForeignKey(LibraryPost, null=True, blank=True, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.content