from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.shortcuts import redirect
import datetime
from recommendation.models import *
# from login.models import user


def recommendation(request):
    posts = Post.objects.all().order_by('-date_time')

    return render(request, 'recommendation/recommendation.html', {'posts' : posts})

def write_form(request):
    get_id = request.session.get('user_id')
    if get_id:
        return render(request, 'recommendation/write_form.html')
    else:
        return HttpResponse('로그인 후 이용해주세요.')

def create(request):
    if request.method == "POST":
        
        user_id = request.session.get('user_id')
        user_game_title = str(request.POST.get('user_game_title'))
        user_game_content = str(request.POST.get('user_game_title'))
        user_game_img = request.FILES.get('user_game_img')
        date_time = datetime.datetime.now()
        
        


        post = Post(user_id = User.objects.get(user_id = user_id),
        user_game_title = user_game_title, 
        user_game_content = user_game_content, 
        user_game_img = user_game_img, 
        date_time = date_time)

        post.save()
    return redirect('recommendation:recommendation')

