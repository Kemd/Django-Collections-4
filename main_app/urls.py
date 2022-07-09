from django.urls import path
from . import views

urlpatterns = [
    # main path/url 
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # route for games 
    path('games/', views.games_index, name='index'),
    path('games/<int:game_id>/', views.games_detail, name='detail'),
    # route for creating 
    path('games/create/', views.GameCreate.as_view(), name='games_create'),
    # route for updating/deleting 
    path('games/<int:pk>/update/', views.GameUpdate.as_view(), name='games_update'),
    path('games/<int:pk>/delete/', views.GameDelete.as_view(), name='games_delete'),
]