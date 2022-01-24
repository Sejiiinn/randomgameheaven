from django.urls import path
from . import views

appname = 'mypage'

urlpatterns = [
    path('', views.mypage, name='mypage')
]