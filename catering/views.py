from django.shortcuts import render, redirect
from .forms import CateringForm
from .models import Catering  # Import the Catering model

def calculate_total_price(food_item, food_quantity, drink_item, drink_quantity):
    # Define the prices for food and drinks
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

    # Calculate the total price
    total_food_price = food_prices.get(food_item, 0.00) * food_quantity
    total_drink_price = drink_prices.get(drink_item, 0.00) * drink_quantity

    return total_food_price + total_drink_price

def catering(request):
    if request.method == 'POST':
        form = CateringForm(request.POST)
        if form.is_valid():
            food_item = form.cleaned_data['food_item']
            drink_item = form.cleaned_data['drink_item']

            # Get quantities from the form
            food_quantity = form.cleaned_data['food_quantity']
            drink_quantity = form.cleaned_data['drink_quantity']
            
            print(f"Food Item: {food_item}, Drink Item: {drink_item}")
            # Calculate the total price
            total_price = calculate_total_price(food_item, food_quantity, drink_item, drink_quantity)
            
            # Create a new instance of Catering and save it
            catering_order = Catering(
                food_item=food_item,
                food_quantity=food_quantity,
                drink_item=drink_item,
                drink_quantity=drink_quantity,
                total_price=total_price
            )
            catering_order.save()

            return redirect('cateringsuccess')
    else:
        form = CateringForm()
    return render(request, 'catering.html', {'form': form})


def cateringsuccess(request):
    return render(request, 'cateringsuccess.html', {})
