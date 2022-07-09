from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('Hello')

def about(request):
    return render(request, 'about.html')

# test data for games 
class Game:
    def __init__(self, name, year, desc, genre, platform):
        self.name = name
        self.year = year
        self.desc = desc
        self.genre = genre
        self.platform = platform

games = [
    Game('Elden Ring', 2022, 'Foul tarnished, put these foolish ambitions to rest', 'Action, Adventure, RPG', 'PC, PS4/PS5, Xbox'),
    Game('Warframe', 2013, 'Space Ninja', 'Action, Adventure, Multiplayer RPG', 'PC'),
    Game('Rocket League', 2015, 'Soccer, but with cars', 'Sport', 'PS4')
]

# game index page 
def games_index(request):
    return render(request, 'games/index.html', {'games': games})
