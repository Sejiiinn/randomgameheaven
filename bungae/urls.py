from django.urls import path
from . import views
app_name = 'bungae'

urlpatterns = [
    path('', views.bungae_board, name = 'bungae'),
]