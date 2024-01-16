from django.urls import path
from . import views

urlpatterns = [
    path('catering/', views.catering, name='catering'),
    path('cateringsuccess/', views.cateringsuccess, name='cateringsuccess'),
]
