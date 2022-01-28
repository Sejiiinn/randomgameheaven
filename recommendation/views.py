from msilib.schema import File
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import datetime
from django.contrib import messages
#from sqlalchemy import null
from recommendation.models import *
from django.core.paginator import Paginator
# from login.models import user


def recommendation(request):
    posts = Post.objects.all().order_by('-date_time')
    # pictures = FileUpload.objects.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 9)
    page = int(page)
    page_obj = paginator.page(page)
    auth = 'notnull'

    start_page = (page - 2)
    end_page = start_page + 4
    if end_page >= paginator.num_pages:
        end_page = paginator.num_pages
        start_page = end_page - 4
    if start_page < 1:
        start_page = 1
        end_page = 5
    if 0 <= paginator.count <= 9:
        end_page = 1
    elif 9 < paginator.count <= 18:
        end_page = 2
    elif 18 < paginator.count <= 27:
        end_page = 3
    elif 27 < paginator.count <= 36:
        end_page = 4
    elif 36 < paginator.count <= 45:
        end_page = 5



    return render(request, 'recommendation/recommendation.html', {'posts' : page_obj, 'auth' : auth, 'page_range' : range(start_page, end_page + 1)})

def write_form(request):
    get_id = request.session.get('user_id')
    if get_id:
        return render(request, 'recommendation/write_form.html')
    else:
        messages.info(request, '로그인 후 이용해주세요.')
        return redirect('recommendation:recommendation')


def create(request):
    if request.method == "POST":
        
        user_id = request.session.get('user_id')
        user_game_title = str(request.POST.get('user_game_title'))
        user_game_content = str(request.POST.get('user_game_content'))
        user_game_img = ""
        try:
            user_game_img = request.FILES['image']
        except:
            user_game_img = "None"
        date_time = datetime.datetime.now()
            
        
        post = Post(user = User.objects.get(user_id = user_id),
        user_game_title = user_game_title, 
        user_game_content = user_game_content, 
        user_game_img = user_game_img, 
        date_time = date_time,
        )


        post.save()
    return redirect('recommendation:recommendation')
