from django.urls import path
from . import views

app_name = 'games'

urlpatterns = [
    path('roulette/', views.roulette, name = 'roulette'),

]