from django.urls import path
from . import views

app_name = 'games'

urlpatterns = [
    # path('roulette/', views.roulette, name = 'roulette'),
    path('hunmin/', views.hunmin, name = 'hunmin'),
    path('randomgame/', views.randomgame, name = 'randomgame'),
    path('roulette/', views.roulette, name = 'roulette'),
    path('moviequiz/', views.moviequiz, name = 'moviequiz'),
    path('rsp/', views.rsp, name = 'rsp'),
    path('keepface/', views.keepface, name = 'keepface'),
]