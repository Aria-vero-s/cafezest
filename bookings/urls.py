from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu', views.menu, name='menu'),
    path('booking', views.booking, name='booking'),
    path('login', views.login_user, name="login"),
    path('logout_user', views.logout_user, name="logout_user"),
    path('register_user', views.register_user, name="register_user"),
    path('notRegistered', views.notRegistered, name="notRegistered"),
    path('account', views.account, name="account"),
    path('edit/<booking_id>', views.bookingEdit, name='edit'),
    path('delete/<booking_id>', views.bookingDelete, name='delete'),
]
