from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.


def bungae_board(request):
    now = datetime.datetime.now()
    nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
    if request.method == 'POST':
        input_text = request.POST.get('input_text')

        result = '%s' % (input_text)
        nickname = str(request.session["nickname"])
        return render(request,
                      'bungae/bungae_board.html', 
                      {'result': result, 'nickname':nickname, 'nowDatetime': nowDatetime})

    return render(request, 'bungae/bungae_board.html')
