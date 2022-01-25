from django.shortcuts import render, redirect
from django.http import HttpResponse
from bungae.models import *
from login.models import user
import datetime

# Create your views here.

def bungae_board(request):

    board = BungaeBoard.objects.all()


    get_id = request.session.get('user_id')

    nickname_list = []

    for nickname in board:
        nickname_list.append(user.objects.get(user_id = str(get_id)).nickname)

    if get_id:
        if request.method == 'POST':
            now = datetime.datetime.now()
            nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')

            input_text = str(request.POST.get('input_text'))
            user_id = str(get_id)
            nickname_list = []

            board = BungaeBoard(User = user.objects.get(user_id = user_id),content = input_text, cre_date = nowDatetime)
            board.save()
            return render(request, 'bungae/bungae_board.html', {'board': board})
    else:
        redirect("bungae : bungae")

    return render(request, 'bungae/bungae_board.html', {'board': board})
