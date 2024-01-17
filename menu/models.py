from django.db import models
from django.contrib.auth.models import User


class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.CharField(max_length=255)
    image = models.ImageField(upload_to='menu_images/')

    def __str__(self):
        return self.name

class Order(models.Model):
    status = models.CharField(max_length=20, default='Not processed')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(MenuItem, through='OrderItem')
    is_paid = models.BooleanField(default=False)
    # Add other fields like delivery address, etc.
    def total_price(self):
        # Calculate the total price of all items in the order
        return sum(item.menu_order.price * item.quantity for item in self.order_items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')  # Change related_name
    menu_order = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    customization = models.CharField(max_length=255, blank=True)
    quantity = models.PositiveIntegerField(default=1)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)