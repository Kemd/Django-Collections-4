from platform import platform
from django.db import models
from django.urls import reverse

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    desc = models.TextField(max_length=250)
    genre = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'game_id': self.id})


