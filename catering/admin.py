from django.contrib import admin
from .models import Catering

@admin.register(Catering)
class CateringAdmin(admin.ModelAdmin):
    list_display = ('food_item', 'food_quantity', 'drink_item', 'drink_quantity', 'total_price')
