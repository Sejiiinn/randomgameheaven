from django.shortcuts import render, redirect
from django.http import HttpResponse
from bungae.models import *
import datetime

# Create your views here.



# def bungae_board(request):
#     now = datetime.datetime.now()
#     nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')

#     if request.method == 'POST':
#         #if request.session.get('user_id'):
#         #input_text = str(request.POST.get('input_text'))
#         #nickname = str(request.session["nickname"])

#         board = BungaeBoard.objects.all()

#         return render(request,
#                       'bungae/bungae_board.html', {'board': board})

#     return render(request, 'bungae/bungae_board.html')

def bungae_board(request):
    now = datetime.datetime.now()
    nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')

    board = BungaeBoard.objects.get(bungae_num = 3)
    board.cre_date = nowDatetime
    board.save()
    return render(request, 'bungae/bungae_board.html', {'board': board})
