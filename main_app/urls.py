from django.urls import path
from . import views

urlpatterns = [
    # main path/url 
    path('', views.home, name='home'),
]