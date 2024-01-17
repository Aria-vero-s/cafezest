from django import template

register = template.Library()

@register.filter
def total_price(order_items):
    return sum(item.menu_order.price if hasattr(item, 'menu_order') else item.price for item in order_items)
