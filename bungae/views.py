from django.shortcuts import render, redirect
from django.http import HttpResponse
from bungae.models import *
#from login.models import user
import datetime
from django.core.paginator import Paginator


#Create your views here.

def bungae_board(request):

    page = request.GET.get('page', 1)

    board = BungaeBoard.objects.all().order_by('-cre_date')

    paginator = Paginator(board, 5)

    page = int(page) # now_page int형 변환 

    page_obj = paginator.page(page)
    
    
    if request.method == 'POST':
        get_id = request.session.get('user_id')
        
        if get_id:
            #nowDatetime = now.strftime('%Y년 %m월 %d일 %H:%M:%S')
            now = datetime.datetime.now()
            input_text = str(request.POST.get('input_text'))
            user_id = str(get_id)
            
            board = BungaeBoard(user = User.objects.get(user_id = user_id),
                                      content = input_text,
                                        cre_date = now,
                                title = '제목없음',
                                post_title = '온라인 번개 모임 게시판')
            
            board.save()

            return redirect ('bungae:bungae')

        else:
            return HttpResponse('로그인 후 이용해주세요.')
    


    return render(request, 'bungae/bungae_board.html', {'board': page_obj})
                                                        # 'page_range' : range(start_page, end_page + 1)})
