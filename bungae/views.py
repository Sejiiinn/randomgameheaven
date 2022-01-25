from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def bungae_board(request):
    return render(request, 'bungae/bungae_board.html')
