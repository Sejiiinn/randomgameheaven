
from django.shortcuts import render
from django.db.models import Max, Avg
from board.models import  Main #/recommendation 모델을 가져와야함
import random

app_name = 'games'

# def get_random_games():
#     max_id = Main.objects.all().aggregate(max_id = Max("id"))['max_id']
#     while True : 
#         pk = random.randint(1, max_id)
#         restaurant = Main.objects.filter(pk=pk).first()
#         if restaurant : 
#             return restaurant

# def roulette(request):
#     restaurant = get_random_games()
#     score_avg = Main.objects.filter(restaurant__name=restaurant.name).aggregate(Avg('score'))

#     return render(request, 'games/roulette.html', {'restaurant':restaurant, 'score_avg':score_avg})

def hunmin(request):
    return render(request, 'games/hunmin.html', {})