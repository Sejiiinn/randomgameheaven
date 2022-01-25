from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def bungae_board(request):
    return render(request, 'bungae/bungae_board.html')

def bungae_board(request):
    if request.method == 'POST':
        a = request.POST.get('a')

        result = '%s' % (a)
        return render(request, 'bungae/bungae_board.html', {'result': result})
    return render(request, 'bungae/bungae_board.html')
