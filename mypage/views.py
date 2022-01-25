from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import board, user
# from .forms import PWChangeForm
# from django.contrib.auth import update_session_auth_hash

def mypage_main(request):
    userid = request.session.get('user_id')
    if userid:
        user_info = user.objects.get(pk=userid)
        user_pw = user_info.user_pw
        nickname = user_info.nickname
        return render(request, 'mypage/mypage.html')
    else:
        return redirect('login:login')
    
# def chage_pw(request):
#     return render(request, 'mypage/change_pw.html')
    
def my_board(request):
    board_list = board.objects.all()
    
    return render(request, 'mypage/mypage.html',
                  {'my_board':my_board})
