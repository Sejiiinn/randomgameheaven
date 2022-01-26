from django.urls import path
from . import views

app_name = 'recommendation'
urlpatterns = [
    path('', views.recommendation, name = 'recommendation'),
    path('write/', views.write_form, name = 'write'),
    path('create/', views.create, name='create'),
]