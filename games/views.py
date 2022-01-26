
from django.shortcuts import render
from django.db.models import Max
from board.models import  Main #/recommendation 모델을 가져와야함
import random



def roulette(request):
 

    return render(request, 'roulette/roulette.html')
