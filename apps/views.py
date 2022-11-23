"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from apps.models import Item
from django.conf import settings
import stripe


def get_item_detail(request, id):
    assert isinstance(request, HttpRequest)

    item = Item.objects.get(pk=id)
    
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
            'item': item
        }
    )


def buy(request, id):
    assert isinstance(request, HttpRequest)

    item = Item.objects.get(pk=id)

    stripe.api_key = settings.STRIPE_API_KEY

    session = stripe.checkout.Session.create(
      success_url="https://example.com/success",
      cancel_url="https://example.com/cancel",
      line_items=[
        {
          "price": item.price_id,
          "quantity": 1,
        },
      ],
      mode="payment",
    )
    
    return JsonResponse({'session_id':session.stripe_id}, status=200)

