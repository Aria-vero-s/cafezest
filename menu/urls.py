from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.menu, name='menu'),
    path('customize_order/<int:item_id>/', views.customize_order, name='customize_order'),
    path('checkout/', views.checkout, name='checkout'),
    path('execute_payment/', views.execute_payment, name='execute_payment'),
    path('cancel_payment/', views.cancel_payment, name='cancel_payment'),
    path('remove_item/<int:item_id>/', views.remove_item, name='remove_item'),
    path('update_quantity/', views.update_quantity, name='update_quantity'),
]