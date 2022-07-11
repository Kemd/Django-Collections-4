from django.shortcuts import render
from django.http import HttpResponse
from .models import Game
from django.views.generic.edit import CreateView, UpdateView, DeleteView
import requests


# Create your views here.
def home(request):
    response = requests.get('https://www.mmobomb.com/api1/games').json()
    return render(request, 'home.html', {'response': response})

def about(request):
    return render(request, 'about.html')

# test data for games 
# class Game:
#     def __init__(self, name, year, desc, genre, platform):
#         self.name = name
#         self.year = year
#         self.desc = desc
#         self.genre = genre
#         self.platform = platform

# games = [
#     Game('Elden Ring', 2022, 'Foul tarnished, put these foolish ambitions to rest', 'Action, Adventure, RPG', 'PC, PS4/PS5, Xbox'),
#     Game('Warframe', 2013, 'Space Ninja', 'Action, Adventure, Multiplayer RPG', 'PC'),
#     Game('Rocket League', 2015, 'Soccer, but with cars', 'Sport', 'PS4')
# ]

# game index page 
def games_index(request):
    games = Game.objects.all()
    return render(request, 'games/index.html', {'games': games})

# game detail page 
def games_detail(request, game_id):
    game = Game.objects.get(id = game_id)
    return render(request, 'games/detail.html', { 'game': game})

# add a game page 
class GameCreate(CreateView):
    model = Game
    fields = ['name', 'year', 'desc', 'genre', 'platform']

# edit a game page 
class GameUpdate(UpdateView):
    model = Game
    fields = ['year', 'desc', 'genre', 'platform']

# delete a game page 
class GameDelete(DeleteView):
    model = Game
    success_url = '/games/'
