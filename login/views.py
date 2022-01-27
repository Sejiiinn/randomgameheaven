from pyexpat.errors import messages
from .models import user
from django.utils import timezone
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages


def signup(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user_pw = request.POST.get('user_pw')
        nickname = request.POST.get('nickname')
        m = user(
            user_id=user_id, user_pw=user_pw, nickname=nickname)
        m.date_joined = timezone.now()
        if user.objects.filter(user_id=user_id).exists():
            return render(request, 'login/signup.html', messages.info(request, '중복된 ID가 존재합니다.'))
        elif user.objects.filter(nickname=nickname).exists():
            return render(request, 'login/signup.html', messages.info(request, '중복된 NickName이 존재합니다.'))
        elif m.user_id == "":
            return render(request, 'login/signup.html', messages.info(request, 'ID를 입력해주세요.'))
        elif m.user_pw == "":
            return render(request, 'login/signup.html', messages.info(request, 'PW를 입력해주세요.'))
        elif m.nickname == "":
            return render(request, 'login/signup.html', messages.info(request, 'nickname을 입력해주세요.'))
        else:
            m.save()    
            return render(request, 'login/login.html', messages.info(request, '회원가입 완료! 로그인해주세요.'))
        
    else:
        #messages.info(request, '테스트입니다.')
        return render(request, 'login/signup.html')


# Create your views here.
def login(request):
    if request.method == 'POST':
        user_id = request.POST.get("user_id")
        user_pw = request.POST.get("user_pw")
        try:
            m = user.objects.get(user_id=user_id, user_pw=user_pw)
        except user.DoesNotExist as e:
            return render(request, 'login/login.html', messages.warning(request, "아이디와 패스워드를 확인해주세요."))
            
        else:
            request.session["user_id"] = m.user_id
            request.session["user_pw"] = m.user_pw
            request.session["nickname"] = m.nickname
        return redirect( 'main:main' )
    else:
        return render(request, 'login/login.html')


def logout(request):

    request.session.flush() # 전체 삭제
    return redirect('main:main')