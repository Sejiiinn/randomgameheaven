from django.shortcuts import render, redirect
from django.http import HttpResponse
from bungae.models import *
from login.models import user
import datetime


#Create your views here.

def bungae_board(request):

    board = BungaeBoard.objects.all().order_by('-cre_date')

    if request.method == 'POST':
          get_id = request.session.get('user_id')

          if get_id:
            #nowDatetime = now.strftime('%Y년 %m월 %d일 %H:%M:%S')

            now = datetime.datetime.now()
            input_text = str(request.POST.get('input_text'))
            user_id = str(get_id)

            board = BungaeBoard(User = user.objects.get(user_id = user_id),
                                content = input_text,
                                cre_date = now,
                                title = '제목없음',
                                post_title = '온라인 번개 모임 게시판')
            board.save()

            return redirect ('bungae:bungae')

          else:
              return HttpResponse('로그인 후 이용해주세요.')

    return render(request, 'bungae/bungae_board.html', {'board': board})


# def bungae_board(request):
    
#     board2 = board.objects.all().order_by('-cre_date')

#     if request.method == 'POST':
#           get_id = request.session.get('user_id')

#           if get_id:
#             #nowDatetime = now.strftime('%Y년 %m월 %d일 %H:%M:%S')

#             now = datetime.datetime.now()
#             input_text = str(request.POST.get('input_text'))
#             userid = str(get_id)
#             it = user.objects.get(user_id = userid)
#             board2 = board(User = it,
#                                 title = '제목없음',
#                                 content = input_text,
#                                 cre_date = now,
#                                 board_type = '온라인 번개 모임 게시판')
#             board2.save()

#             return redirect ('bungae:bungae')

#           else:
#               return HttpResponse('로그인 후 이용해주세요.')

#     return render(request, 'bungae/bungae_board.html', {'board': board2})

      



