from django.urls import path
from . import views
from .views import test

urlpatterns = [
    path('', views.index, name='index'),
    path('test/', test, name='test'),
    path('error/', views.error, name='error'),
    path('menu', views.menu, name='menu'),
]