from django.forms import ModelForm
from .models import PlayDate

class PlayDateForm(ModelForm):
    class Meta:
        model = PlayDate
        fields = ['date']