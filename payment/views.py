import stripe
from django.conf import settings
from django.http import JsonResponse
from order.models import Order
from django.shortcuts import render, redirect

stripe.api_key = settings.STRIPE_SECRET_KEY


def create_checkout_session(request, pk):
    YOUR_DOMAIN = 'http://127.0.0.1:8000'
    order = Order.objects.get(id=pk)
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': 'rub',
                    'unit_amount_decimal': (order.get_total_cost() * 100),
                    'product_data': {
                        'name': f'Номер заказа {order.id}'
                    }
                },
                'quantity': 1,
            },
        ],
        mode='payment',
        success_url=YOUR_DOMAIN + '/payment/success',
        cancel_url=YOUR_DOMAIN + '/payment/cancel',
    )

    return redirect(checkout_session.url, code=303)


def success_payment(request):
    return render(request, 'payment/success.html')


def cansel_payment(request):
    return render(request, 'payment/cansel.html')
