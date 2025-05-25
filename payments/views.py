import stripe
from django.shortcuts import render
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY

def checkout(request):
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': 'Test Product',
                },
                'unit_amount': 200,  # قیمت (2 دلار)
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='http://127.0.0.1:8000/success/',
        cancel_url='http://127.0.0.1:8000/cancel/',
    )
    return render(request, 'checkout.html', {
        'session_id': session.id,
        'stripe_public_key': settings.STRIPE_PUBLISHABLE_KEY,
    })

def success(request):
    return render(request, 'success.html')

def cancel(request):
    return render(request, 'cancel.html')
