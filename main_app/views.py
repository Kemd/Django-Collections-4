from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Game
from django.views.generic.edit import CreateView, UpdateView, DeleteView
import requests
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


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
@login_required
def games_index(request):
    games = Game.objects.filter(user=request.user)
    return render(request, 'games/index.html', {'games': games})

# game detail page
@login_required 
def games_detail(request, game_id):
    game = Game.objects.get(id = game_id)
    return render(request, 'games/detail.html', { 'game': game})

# add a game page 
class GameCreate(LoginRequiredMixin, CreateView):
    model = Game
    fields = ['name', 'year', 'desc', 'genre', 'platform']

    success_url = '/games/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# edit a game page 
class GameUpdate(LoginRequiredMixin, UpdateView):
    model = Game
    fields = ['year', 'desc', 'genre', 'platform']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# delete a game page 
class GameDelete(LoginRequiredMixin, DeleteView):
    model = Game
    success_url = '/games/'


# Singup page 
def signup(request):
    err_msg = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            err_msg = 'Invalid - Please try again'
    form = UserCreationForm()
    context = {'form': form, 'err_msg': err_msg}
    return render(request, 'registration/signup.html', context)
