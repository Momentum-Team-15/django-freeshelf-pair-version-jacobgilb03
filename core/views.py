from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import User, Podcast, Category, Favorite
# from .forms import FavoriteForm

# Create your views here.

@login_required
def list_podcasts(request):
    favorites = [favorite.podcast for favorite in request.user.favorites.all()]
    podcasts = Podcast.objects.all().order_by("created_date")
    return render(request, 'core/podcast_list.html', {'podcasts': podcasts, 'favorites': favorites})

def favorite_podcasts(request):
    favorites = request.user.favorites.all()
    return render(request, 'core/favorite_podcasts.html', {"favorites": favorites})

def add_favorite(request, podcast_id):
    podcast = Podcast.objects.get(id=podcast_id)
    favorite = Favorite.objects.create(user=request.user, podcast=podcast)
    favorite.save()
    return redirect(to='list_podcasts')

def remove_favorite(request, podcast_id):
    podcast = Podcast.objects.get(id=podcast_id)
    favorite = Favorite.objects.get(user=request.user, podcast=podcast)
    favorite.delete()
    return redirect(to='list_podcasts')

def podcasts_by_category(request, slug):
    category = Category.objects.get(slug=slug)
    podcasts = Podcast.objects.filter(category=category)

    return render(request, 'core/podcasts_by_category.html',{"podcasts":podcasts, "category":category})




# categories = Podcast.objects.filter(category__contains="JavaScript")