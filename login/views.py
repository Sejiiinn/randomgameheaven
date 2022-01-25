from .models import user
from django.utils import timezone
from django.http import HttpResponse
from django.shortcuts import render, redirect



def signup(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user_pw = request.POST.get('user_pw')
        nickname = request.POST.get('nickname')

        m = user(
            user_id=user_id, user_pw=user_pw, nickname=nickname)
        m.date_joined = timezone.now()
        m.save()

        return HttpResponse(
            '가입 완료<br>%s %s %s' % (user_id, user_pw, nickname))
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
            return HttpResponse('로그인 실패')
        else:
            request.session["user_id"] = m.user_id
            request.session["user_pw"] = m.nickname
        return redirect( 'main:main' )
    else:
        return render(request, 'login/login.html')