from .models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Podcast

# class PodcastForm(forms.ModelForm):
#     class Meta:
#         model = Podcast
#         fields = [
#             'title',
#             'author_name',
#             'description',
#             'url'
#         ]