from django.contrib import admin
from .models import User, Podcast, Category, Favorite

# Register your models here.
admin.site.register(User)
admin.site.register(Podcast)
admin.site.register(Category)
admin.site.register(Favorite)