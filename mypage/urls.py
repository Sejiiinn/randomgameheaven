from django.urls import path
from . import views

app_name = 'mypage'

urlpatterns = [
    path('', views.mypage_main, name='mypage_main'),
    path('change_pw/', views.chage_pw, name='change_pw'),
]