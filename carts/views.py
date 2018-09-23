from django.shortcuts import render, redirect
from accounts.forms import LoginForm, GuestForm
from orders.models import Order
from product.models import Product
from billing.models import BillingProfile
from addresses.forms import AddressForm
from addresses.models import Address
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


def checkout_home(request):
    cart_obj, cart_created = Cart.objects.new_or_get(request)
    order_obj = None
    if cart_created or cart_obj.product.count() == 0:
        return redirect("cart")
    login_form = LoginForm()
    guest_form = GuestForm()
    address_form = AddressForm()
    billing_address_id = request.session.get("billing_address_id", None)
    shipping_address_id = request.session.get("shipping_address_id", None)

    billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
    print(billing_profile)
    address_qs = None
    if billing_profile is not None:
        if request.user.is_authenticated:
            address_qs = Address.objects.filter(billing_profile=billing_profile)
            print(address_qs)
        order_obj, order_obj_created = Order.objects.new_or_get(billing_profile, cart_obj)
        if shipping_address_id:
            order_obj.shipping_address = Address.objects.get(id=shipping_address_id)
            del request.session["shipping_address_id"]
        if billing_address_id:
            order_obj.billing_address = Address.objects.get(id=billing_address_id)
            del request.session["billing_address_id"]
        if billing_address_id or shipping_address_id:
            order_obj.save()
    if request.method == "POST":
        'some check that order is done'
        is_done=order_obj.check_done()
        if is_done:
            order_obj.mark_paid()
            request.session['cart_items'] = 0
            del request.session['cart_id']
            return redirect("success")
    context = {
        "object": order_obj,
        "billing_profile": billing_profile,
        "login_form": login_form,
        "guest_form": guest_form,
        "address_form": address_form,
        "address_qs": address_qs
        # "billing_address_form": billing_address_form
    }
    return render(request, "carts/checkout.html", context)


def chechout_done_view(request):
    billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
    cart_obj, cart_created = Cart.objects.new_or_get(request)
    billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
    print(billing_profile)
    address_qs = None
    if billing_profile is not None:
        if request.user.is_authenticated:
            address_qs = Address.objects.filter(billing_profile=billing_profile)
        order_obj, order_obj_created = Order.objects.new_or_get(billing_profile, cart_obj)
    context = {
        "object": order_obj,
    }
    return render(request, "carts/checkout-done.html", context)



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