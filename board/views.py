from django.shortcuts import render
from django.http import HttpResponse

from .models import Main
def main(request):
    prd = request.GET.get('prd')
    maindata = Main.objects.all()

    return render(
        request, 'board/main.html', 
        { 'data' : maindata  })