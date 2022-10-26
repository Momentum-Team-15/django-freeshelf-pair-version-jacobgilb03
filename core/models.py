from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class User(AbstractUser):
    favorite_podcasts = models.ManyToManyField('Podcast')

class Podcast(models.Model):
    title = models.CharField(max_length=200)
    host = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    url = models.URLField(max_length=100, null=True, blank=True)


    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=50)

# class SlugField(max_length = 50, **options)