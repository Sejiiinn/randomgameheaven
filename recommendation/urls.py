from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'recommendation'
urlpatterns = [
    path('', views.recommendation, name = 'recommendation'),
    path('write/', views.write_form, name = 'write'),
    path('create/', views.create, name='create'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)