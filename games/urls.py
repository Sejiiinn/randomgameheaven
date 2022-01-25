from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'games'

urlpatterns = [
    path('roulette/', views.roulette, name = 'roulette'),

]