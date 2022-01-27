from django.urls import path
from . import views

app_name = 'mypage'

urlpatterns = [
    path('', views.mypage_main, name='mypage_main'),
    path('change_pw/', views.change_pw, name='change_pw'),
    path('change_nm/', views.change_nm, name='change_nm'),
]