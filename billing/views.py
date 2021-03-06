from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.utils.http import is_safe_url

import stripe
stripe.api_key = 'sk_test_75Ub2sZFkpTuXbu79bkJZAyZ'
STRIPE_PUB_KEY = 'pk_test_o1ZtyaiQ0vwiE65OzQrSwFGF'

def payment_method_view(request):
    next_url = None
    next_ = request.GET.get('next')
    if is_safe_url(next_, request.get_host()):
        next_url = next_
    return render(request, 'carts/checkout-done.html', {"publish_key": STRIPE_PUB_KEY})

def payment_method_createview(request):
    if request.method == 'POST' and request.is_ajax():
        print(request.POST)
        return JsonResponse({"message": "Done"})
    raise HttpResponse("error", status_code=401)
