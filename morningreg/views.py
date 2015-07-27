from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import NameForm
from .models import *
from datetime import datetime
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            new_player = form.cleaned_data['Name']
            addPlayer = Player(name=new_player)
            addPlayer.save()
        return HttpResponseRedirect(reverse('reg:index'))
    else:
        form = NameForm()
        players = Player.objects.all()
        day = Day.objects.get(pk=1)
        context = {'form': form, 'players': players, 'day': day }
    return render(request, 'index.html', context)

def refresh(request):
    day = Day.objects.get(pk=1)
    currentTime = datetime.now()
    minutes = currentTime.hour * 60 + currentTime.minute
    if minutes > 1029 and minutes < 1032:
        if currentTime.weekday() == 0:
            players = Player.objects.all().delete()
            day.name="Wednesday"
        if currentTime.weekday() == 2:
            players = Player.objects.all().delete()
            day.name="Friday"
        if currentTime.weekday() == 4:
            players = Player.objects.all().delete()
            day.name="Monday"
        day.save()
    
    return HttpResponse("Refresh Complete")