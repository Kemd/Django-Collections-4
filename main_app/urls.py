from django.urls import path
from . import views

urlpatterns = [
    # main path/url 
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # route for games 
    path('games/', views.games_index, name='index'),
]