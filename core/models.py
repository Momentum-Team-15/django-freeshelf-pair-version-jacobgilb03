from django.db import models
from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import slugify
from django.urls import reverse


class User(AbstractUser):
    def __repr__(self):
        pass

class Podcast(models.Model):
    title = models.CharField(max_length=200)
    host = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    url = models.URLField(max_length=100, null=True, blank=True)


    def __str__(self):
        return self.title

    # @property
    # def check_favorites(self, user):
    #     favorite_podcasts = [favorite.resource for favorite in user.favorites]
    #     if self in favorite_podcasts:
    #         return True

class Category(models.Model):
    title = models.CharField(max_length = 200, null=True)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category_detail', kwargs = {'slug':self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
        return super().save(*args, **kwargs) 



class Favorite(models.Model):
    podcast = models.ForeignKey('Podcast', related_name='favorites', on_delete=models.CASCADE)
    user    = models.ForeignKey('User', related_name='favorites',on_delete=models.CASCADE)


