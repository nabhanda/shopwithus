from django.shortcuts import render, redirect

from product.models import Product
from .models import Cart

def cart_home(request):
       cart_obj, new_obj = Cart.objects.new_or_get(request)
       return render(request, "carts/home.html", {})

def cart_update(request):
    product_id = 12
    product_obj = Product.objects.get(id=product_id)
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    cart_obj.product.add(product_obj)
    return redirect(product_obj.get_absolute_url())




##############Working Cart view but do not have user association###############
# def cart_home(request):
#     #del request.session['cart_id']
#     cart_id = request.session.get("cart_id", None)
#     if cart_id is None: #and isinstance(cart_id, int):
#         cart_obj = Cart.objects.create(user=None)
#         request.session['cart_id'] = cart_obj.id
#         print('New Cart created')
#     else:
#         print('Cart id exists')
#         print(cart_id)
#         #cart_obj = Cart.objects.get(id=cart_id)
#     return render(request,"carts/home.html", {})