from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .models import Podcast
from django.contrib.auth.decorators import login_required

# Create your views here.

def list_podcasts(request):
    podcasts = Podcast.objects.all.order_by("created_date")
    return render(request, 'core/podcast_list.html', {'podcasts': podcasts})

  