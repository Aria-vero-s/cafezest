from django.contrib import admin
from .models import MenuItem, Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'is_paid']
    inlines = [OrderItemInline]


admin.site.register(MenuItem)
admin.site.register(Order, OrderAdmin)
