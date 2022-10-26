from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import User, Podcast

# Create your views here.

@login_required
def list_podcasts(request):
    podcasts = Podcast.objects.all().order_by("created_date")
    return render(request, 'core/podcast_list.html', {'podcasts': podcasts})

# def list_categories(request):
    

def favorite_podcasts(request):
    user = User.objects.get(id=request.user.id)
    podcasts = user.favorite_podcasts.all()
    return render(request, 'core/favorite_podcasts.html', {"user":user, "podcasts": podcasts})

def add_favorite(request, podcast_id):
    podcast = Podcast.objects.get(id=podcast_id)
    user = User.objects.get(id=request.user.id)
    user.favorite_podcasts.add(podcast)
    return redirect(to='podcast_list')

def remove_favorite(request, podcast_id):
    podcast = Podcast.objects.get(id=podcast_id)
    user = user.objects.get(id=request.user.id)
    user.favorite_podcasts.remove(podcast)
    return redirect(to='podcast_list')

# categories = Podcast.objects.filter(category__contains="JavaScript")