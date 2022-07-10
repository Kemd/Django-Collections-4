from platform import platform
from django.db import models
from django.urls import reverse

# Create your models here.
# Game model 
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


# Play date 
class PlayDate(models.Model):
    date = models.DateField('Dates you played')

    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return f"Played on {self.date}"

    class Meta:
        ordering = ['-date']
    

