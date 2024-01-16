from django.db import models

class Catering(models.Model):
    # Define choices for food and drink items
    FOOD_CHOICES = [
        ('croissant', 'Croissant ($1)'),
        ('sandwich', 'Sandwich ($6)'),
        ('salad', 'Salad ($5)'),
        ('pastry', 'Pastry ($2)'),
    ]

    DRINK_CHOICES = [
        ('latte', 'Latte ($3)'),
        ('coffee', 'Coffee ($2)'),
        ('tea', 'Tea ($1)'),
        ('juice', 'Juice ($1)'),
    ]

    food_item = models.CharField(max_length=255, choices=FOOD_CHOICES)
    food_quantity = models.PositiveIntegerField()
    drink_item = models.CharField(max_length=255, choices=DRINK_CHOICES)
    drink_quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def save(self, *args, **kwargs):
        # Calculate the total price based on food and drink choices
        food_prices = {
            'croissant': 1.00,
            'sandwich': 6.00,
            'salad': 5.00,
            'pastry': 2.00,
        }

        drink_prices = {
            'latte': 3.00,
            'coffee': 2.00,
            'tea': 1.00,
            'juice': 1.00,
        }

        total_food_price = food_prices.get(self.food_item, 0.00) * self.food_quantity
        total_drink_price = drink_prices.get(self.drink_item, 0.00) * self.drink_quantity

        self.total_price = total_food_price + total_drink_price
        super(Catering, self).save(*args, **kwargs)
