from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class User(AbstractUser):
    pass

class Podcast(models.Model):
    title = models.CharField(max_length=200)
    host = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    url = models.URLField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.title