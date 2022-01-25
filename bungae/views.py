from django.shortcuts import render, redirect
from django.http import HttpResponse
from bungae.models import *
from login.models import user
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

# def bungae_board(request):

#     board = BungaeBoard.objects.last()

#     return render(request, 'bungae/bungae_board.html', {'board': board})

def bungae_board(request):

    board = BungaeBoard.objects.all()

    get_id = request.session.get('user_id')

    if get_id:
        if request.method == 'POST':
            now = datetime.datetime.now()
            nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')

            input_text = str(request.POST.get('input_text'))
            user_id = str(get_id)

            board = BungaeBoard(User = user.objects.get(user_id = user_id),content = input_text, cre_date = nowDatetime)
            board.save()
            return render(request, 'bungae/bungae_board.html', {'board': board})


    return render(request, 'bungae/bungae_board.html', {'board': board})
