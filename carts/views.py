from django.shortcuts import render, redirect

from product.models import Product
from .models import Cart

def cart_home(request):
       cart_obj, new_obj = Cart.objects.new_or_get(request)
       return render(request, "carts/home.html", {"cart":cart_obj})

def cart_update(request):
    product_id = request.POST.get('product_id')
    if product_id is not None:
        try:
            product_obj = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            print("May be Product is no more listed. Try after some time")
            return redirect("cart")
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    if product_obj in cart_obj.product.all():
        cart_obj.product.remove(product_obj)
    else:
        cart_obj.product.add(product_obj)
    request.session['cart_items'] = cart_obj.product.count()
    #return redirect(product_obj.get_absolute_url())
    return redirect("cart")




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