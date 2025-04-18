from datetime import datetime

from django.shortcuts import get_object_or_404, redirect, render
from django.template.defaultfilters import length
from django.views import View

from accounts.models import Address
from home.models import Product
from orders.models import Coupon

from orders.cart import Cart
from orders.forms import CouponForm


class CartAddView(View):
    def get(self, request):
        cart = Cart(request)
        if cart :
            return render(request, 'orders/cart-detail.html', {'cart':cart})
        else:
            return render(request, 'orders/cart-empty.html' )
    def post(self,request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        color = request.POST.get('color')
        quantity = request.POST.get('quantity')
        cart.add(product, int(quantity), color)
        return redirect('home:detail_product', product_id)

class CartDeleteView(View):
    def get(self, request, product_id, color):
        cart = Cart(request)
        cart.delete(product_id, color)
        return redirect('home:detail_product', product_id)

# class CouponApplyView(View):
#     form_class =CouponForm
#     def post(self,request):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             now = datetime.now()
#             coupon = Coupon.objects.get(code__exact=form.cleaned_data['code'], valid_from__lte=now, valid_to__gt=now,active=True)
#             if coupon:
#                 cart = Cart(request)
#                 cart.total_price(coupon.discount)

class OrderCreateView(View):
    def dispatch(self, request, *args, **kwargs):
        if Address.objects.filter(user=request.user).exists():
            return super().dispatch(*args, **kwargs)
        return redirect('accounts:address_list')

