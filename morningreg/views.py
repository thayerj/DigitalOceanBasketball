from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import NameForm
from .models import *
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
        context = {'form': form, 'players': players }
    return render(request, 'index.html', context)