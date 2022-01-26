from django.urls import path
from . import views

app_name = 'games'

urlpatterns = [
    # path('roulette/', views.roulette, name = 'roulette'),
    path('hunmin/', views.hunmin, name = 'hunmin'),
    path('roulette/', views.roulette, name = 'roulette'),
    path('initialquiz/', views.initialquiz, name = 'initialquiz'),
    path('rsp/', views.rsp, name = 'rsp'),
]