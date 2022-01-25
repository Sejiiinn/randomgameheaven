from email import message
from pyexpat.errors import messages
from .models import user
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
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
        m.save()
        messages.info(request, '회원가입이 완료되었습니다.')
        return HttpResponseRedirect('login'+nickname)
    else:
        return render(request, 'login/signup.html')


# Create your views here.
def login(request):
    if request.method == 'POST':
        user_id = request.POST.get("user_id")
        user_pw = request.POST.get("user_pw")
        try:
            m = user.objects.get(user_id=user_id, user_pw=user_pw)
        except user.DoesNotExist as e:
            return render(request, 'login/login.html', messages.warning(request, "아이디와 패스워드를 확인하세요."))
            
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