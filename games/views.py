
from django.shortcuts import render
from django.db.models import Max
from board.models import  Main #/recommendation 모델을 가져와야함
import random

app_name = 'games'

def hunmin(request):
    return render(request, 'games/hunmin.html', {})



def randomgame(request):
    return render(request, 'games/randomgame.html')
    
def roulette(request):
    return render(request, 'games/roulette.html')

def moviequiz(request):
    return render(request, 'games/moviequiz.html')

def rsp(request):
    return render(request, 'games/rsp.html')