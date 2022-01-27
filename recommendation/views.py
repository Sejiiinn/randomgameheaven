from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import datetime

#from sqlalchemy import ForeignKey
from recommendation.models import *
from django.core.paginator import Paginator
# from login.models import user


def recommendation(request):
    posts = Post.objects.all().order_by('-date_time')

    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 9)
    page = int(page)
    page_obj = paginator.page(page)
    auth = 'notnull'

    start_page = (page - 1) // 6 * 6 + 1
    end_page = start_page + 5
    if end_page > paginator.num_pages:
        end_page = paginator.num_pages


    return render(request, 'recommendation/recommendation.html', {'posts' : page_obj, 'auth' : auth, 'page_range' : range(start_page, end_page + 1)})

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
        
        


        post = Post(user = User.objects.get(user_id = user_id),
        user_game_title = user_game_title, 
        user_game_content = user_game_content, 
        user_game_img = user_game_img, 
        date_time = date_time)

        post.save()
    return redirect('recommendation:recommendation')
