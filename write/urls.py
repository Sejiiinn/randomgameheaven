from django.urls import path
from . import views

app_name = 'write'
urlpatterns = [
    path('', views.write_form, name = 'write'),
]