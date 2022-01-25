from django.shortcuts import redirect, render
from django.http import HttpResponse

from mypage.forms import ChangePasswordForm
from .models import board, user
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

from bungae.models import BungaeBoard

def mypage_main(request):
    userid = request.session.get('user_id')
    board = BungaeBoard.objects.filter(User = str(userid)).order_by('-cre_date')

    if userid:
        user_info = user.objects.get(pk=userid)
        user_pw = user_info.user_pw
        nickname = user_info.nickname
        return render(request, 'mypage/mypage.html', {'board' : board})
    else:
        return redirect('login:login')

def chage_pw(request):
    if request.method == 'POST':
        change_pw_form = ChangePasswordForm(request.user, request.POST)
        if change_pw_form.is_valid():
            user = change_pw_form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "비밀번호가 변경되었습니다.")
            return redirect('mypage:mypage_main')
    else:
        change_pw_form = ChangePasswordForm(request.user)
    
    return render(request, 'mypage/change_pw.html', {'change_pw_form':change_pw_form})
    
def my_board(request):
    board_list = board.objects.all()
    
    return render(request, 'mypage/mypage.html',
                  {'my_board':my_board})