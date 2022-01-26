from django.shortcuts import render
from django.http import HttpResponse
from .models import POST
from django.shortcuts import redirect

def recommendation(request):
    posts = POST.objects

    return render(request, 'recommendation/recommendation.html', {'posts' : posts})


def write_form(request):
    return render(request, 'recommendation/write_form.html')

def create(request):
    if(request.method == "POST"):
        post = POST()
        # post.user_game_id = request.POST['title']
        # post.user_id = request.POST['title']
        post.user_game_title = request.POST['title']
        post.user_game_content = request.POST['content']
        # post.user_game_img = request.POST['title']
        # post.date_time = request.POST['title']
        post.save()
    return redirect(recommendation)