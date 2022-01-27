from gettext import translation
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import User, Usergame
from bungae.models import *
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse

from bungae.models import BungaeBoard

def mypage_main(request):
    userid = request.session.get('user_id')
    #board = BungaeBoard.objects.filter(User = str(userid)).order_by('-cre_date')


    if userid:
        user_info = User.objects.get(user_id=userid)
        user_pw = user_info.user_pw
        nickname = user_info.nickname
        
        bungae = BungaeBoard.objects.filter(user=user_info.user_id) # 변수명 User -> user로 변경
        user_game = Usergame.objects.filter(user=user_info.user_id)

        if request.method == 'POST':
            a = request.POST.get('a')
            a = int(a)
            post = BungaeBoard.objects.get(bungae_num = a)
            post.delete()
        
        return render(request,
                      'mypage/mypage.html',
                      {'bungae':bungae,
                       'usergame':user_game,
                       'nickname':nickname
                       })
    else:
        return redirect('login:login')

def change_pw(request):
    userid = request.session.get('user_id')
    userpw = request.session.get('user_pw')
    usernickname = request.session.get('nickname')
    
    if request.method=='POST':
        old_pw = str(request.POST.get('old_pw'))
        new_pw = str(request.POST.get('new_pw'))
        new2_pw = str(request.POST.get('new2_pw'))
        
        if userpw == old_pw:
            user_info = User.objects.get(user_id=userid)
            user_info.user_pw = new2_pw
            user_info.save()
            request.session["user_pw"] = new2_pw
            # messages.info(request, "비밀번호가 변경되었습니다.")
            return redirect('mypage:mypage_main')
        elif new_pw != new2_pw:
            messages.info(request, '변경할 비밀번호가 서로 다릅니다.')
            return redirect('mypage:change_pw')
        elif userpw != old_pw:
            messages.info(request, '현재 비밀번호가 다릅니다.')
            return redirect('mypage:change_pw')
        else:
            messages.info(request, '비밀번호를 입력하세요.')
            return redirect('mypage:change_pw')
        
    return render(request, 'mypage/change_pw.html')

def change_nm(request):
    userid = request.session.get('user_id')
    usernickname = request.session.get('nickname')
    
    if request.method == 'POST':
        new_nickname = str(request.POST.get('new_nm'))
        
        if usernickname != new_nickname:
            user_info = User.objects.get(user_id=userid)
            user_info.nickname = new_nickname
            request.session['nickname'] = new_nickname
            user_info.save()
            # messages.info(request, '닉네임이 변경되었습니다.')
            return redirect('mypage:mypage_main')
        elif new_nickname == '':
            messages.info(request, '다시 입력하세요.')
            return redirect(reverse('mypage:change_nm'))
        else:
            messages.info(request, '다시 입력하세요.')
            return redirect(reverse('mypage:change_nm'))
        
    return render(request, 'mypage/change_nm.html')

    
def usergame_delete(request):
    if request.method == 'POST':
        ugameid = int(request.POST.get("hidid"))
        user_game_del = Usergame.objects.get(user_game_id=ugameid)
        user_game_del.delete()
        messages.success(request, "삭제되었습니다.")
        return redirect('mypage:mypage')