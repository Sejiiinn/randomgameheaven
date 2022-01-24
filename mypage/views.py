from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Board, User

def mypage_main(request):
    try:
        user_id = request.session['user_id']
        nickname = request.session['nickname']
        return render(request, 'mypage/mypage.html')
     
    except:
        return redirect('login')
    
def my_board(request):
    board_list = Board.objects.all()
    
    return render(request, 'mypage/mypage.html',
                  {'my_board':my_board})