from django.shortcuts import render, get_object_or_404, redirect
from .models import MenuItem, Order, OrderItem, UserProfile
from .forms import OrderItemForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from paypal.standard.forms import PayPalPaymentsForm
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from paypal.standard.ipn.signals import valid_ipn_received
from django.dispatch import receiver
import paypalrestsdk
from django.contrib.auth.decorators import login_required

paypalrestsdk.configure({
    "mode": "sandbox",
    "client_id": "AWlSvLJeKoDnNgvyeM9PziAkPBw0esbIN--mil-NHOFq03PIn-Iw-74FBiIBmN6v0gHAgs_ARAL45RGv",
    "client_secret": "EAUbAIPNH5hv-7glW1UytVbZjobSnOODw9q8T-1p6nQupcsbsSRsIjLfPAusQ7YJEiGUPYJnE7umQimj",
})


def menu(request):
    menu_items = MenuItem.objects.all()
    context = {'menu_items': menu_items}
    return render(request, 'menu.html', context)


def customize_order(request, item_id):
    print("Received item ID:", item_id)
    menu_order = get_object_or_404(MenuItem, id=item_id)

    if request.method == 'POST':
        form = OrderItemForm(request.POST)
        if form.is_valid():
            customization = form.cleaned_data['customization']
            quantity = form.cleaned_data['quantity']

            user_profile, created = UserProfile.objects.get_or_create(user=request.user)
            order, created = Order.objects.get_or_create(user=request.user)

            order_item, created = OrderItem.objects.get_or_create(order=order, menu_order=menu_order, customization=customization)
            
            # Update quantity if the item already exists
            if not created:
                order_item.quantity += quantity
                order_item.save()

            return redirect('checkout')

    else:
        form = OrderItemForm()

    context = {
        'form': form,
        'menu_order': menu_order,
    }

    return render(request, 'customize_order.html', context)


def checkout(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
        order = Order.objects.get(userprofile=user_profile)
    except UserProfile.DoesNotExist:
        user_profile = None
        order = None

    item_id = None
    if order and order.order_items.exists():
        item_id = order.order_items.first().menu_order.id if order.order_items.first().menu_order else None

    if request.method == 'POST':
        # Calculate the total amount based on order items
        total_amount = order.total_price()  # Use the correct method here

        # Create a payment
        payment = paypalrestsdk.Payment({
            "intent": "sale",
            "payer": {
                "payment_method": "paypal",
            },
            "transactions": [
                {
                    "amount": {
                        "total": str(total_amount),  # Convert total_amount to string
                        "currency": "USD",
                    },
                    "description": "Payment for cafe order",
                }
            ],
            "redirect_urls": {
                "return_url": request.build_absolute_uri('execute_payment/'),
                "cancel_url": request.build_absolute_uri('cancel_payment/'),
            },
        })

        if payment.create():
            # Redirect to PayPal for user confirmation
            for link in payment.links:
                if link.method == "REDIRECT":
                    return redirect(link.href)

    context = {
        'order': order,
        'item_id': item_id,
    }

    return render(request, 'checkout.html', context)


def payment_successful(request):
    # Handle successful payment
    return render(request, 'payment_successful.html')

def payment_cancelled(request):
    # Handle canceled payment
    return render(request, 'payment_cancelled.html')


@receiver(valid_ipn_received)
def ipn_receiver(sender, **kwargs):
    ipn_obj = sender
    # Process the IPN data and update your application accordingly
    # Example: Update order status, inventory, etc.
    if ipn_obj.payment_status == "Completed":
        # Update your order status logic here
        order_id = ipn_obj.invoice
        try:
            order = Order.objects.get(id=order_id)
            order.status = 'Completed'  # Update this line based on your actual status field
            order.save()
        except Order.DoesNotExist:
            # Handle the case where the order is not found
            pass

@require_POST
@csrf_exempt
def paypal_webhook(request):
    # Respond to PayPal with an HTTP 200 OK status
    return HttpResponse(status=200)

def execute_payment(request):
    payment_id = request.GET.get('paymentId')
    payer_id = request.GET.get('PayerID')

    payment = paypalrestsdk.Payment.find(payment_id)

    if payment.execute({"payer_id": payer_id}):
        # Payment successful, update your order status or perform necessary actions
        return render(request, 'payment_success.html')
    else:
        # Payment failed, handle accordingly
        return render(request, 'payment_failure.html')

def cancel_payment(request):
    # Handle payment cancellation, redirect to an appropriate page
    return render(request, 'payment_cancel.html')

@login_required
def remove_item(request, item_id):
    item = get_object_or_404(OrderItem, id=item_id)
    print(f"Removing item: {item}")
    item.delete()
    return redirect('checkout')