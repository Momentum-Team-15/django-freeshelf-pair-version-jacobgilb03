from django.urls import include
"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views
from core import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
    path('', views.list_podcasts, name='list_podcasts'),
    path("accounts/", include("django.contrib.auth.urls")),
    path('podcasts/favorites/', views.favorite_podcasts, name="favorite_podcasts"),
    path('podcasts/favorite/add/<int:podcast_id>', views.add_favorite, name="add_favorite"),
    path('podcasts/favorite/remove/<int:podcast_id>', views.remove_favorite, name="remove_favorite"),
    # path('resources/comedy', views.list_categories, name="comedy")
]
