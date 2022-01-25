from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.


def bungae_board(request):
    if request.method == 'POST':
        input_text = request.POST.get('input_text')

        result = '%s' % (input_text)
        now = datetime.datetime.now()
        nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
        return render(request,
                      'bungae/bungae_board.html', 
                      {'result': result, 'user_id':request.session["user_id"], 'nowDatetime': nowDatetime})

    return render(request, 'bungae/bungae_board.html')
