from django.shortcuts import render
from django.http import HttpResponse


def write_form(request):
    return render(request, 'write/write_form.html')