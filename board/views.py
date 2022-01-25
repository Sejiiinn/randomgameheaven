from django.shortcuts import render
from django.http import HttpResponse

from .models import Main
def main(request):
    search = request.GET.get('search')
    if search:
        maindata = Main.objects.filter(game_title__contains = search)
    else:
        maindata = Main.objects.all()

    return render(
        request, 'board/main.html', 
        { 'data' : maindata  })