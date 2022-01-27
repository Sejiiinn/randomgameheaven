
from django.shortcuts import render
from django.db.models import Max
from board.models import  Main #/recommendation 모델을 가져와야함
import random
from games.models import MovieQuiz

app_name = 'games'

def hunmin(request):
    return render(request, 'games/hunmin.html', {})



def randomgame(request):
    return render(request, 'games/randomgame.html')
    
def roulette(request):
    return render(request, 'games/roulette.html')

def moviequiz(request):

    moviequiz = MovieQuiz.objects.all()
    return render(request, 'games/moviequiz.html', {'moviequiz': moviequiz})

def rsp(request):
    return render(request, 'games/rsp.html')

def keepface(request):
    return render(request, 'games/keepface.html')