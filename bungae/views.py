from django.shortcuts import render, redirect
from django.http import HttpResponse
from bungae.models import *
from login.models import user
import datetime
from django.contrib import messages
#from django.utils import timezone

# Create your views here.

def bungae_board(request):

    board = BungaeBoard.objects.all().order_by('-cre_date')

    if request.method == 'POST':
          get_id = request.session.get('user_id')

          if get_id:
            #now = timezone.now()
            #nowDatetime = now.strftime('%Y년 %m월 %d일 %H:%M:%S')

            now = datetime.datetime.now()
            input_text = str(request.POST.get('input_text'))
            user_id = str(get_id)

            board = BungaeBoard(User = user.objects.get(user_id = user_id),content = input_text, cre_date = now)
            board.save()

            return HttpResponse('게시글이 작성 되었습니다.')

          else:
              return HttpResponse('로그인 후 이용해주세요.')

    return render(request, 'bungae/bungae_board.html', {'board': board})




