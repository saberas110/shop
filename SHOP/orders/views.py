from django.shortcuts import get_object_or_404, redirect
from django.template.defaultfilters import length
from django.views import View
from home.models import Product

from orders.cart import Cart


class CartAddView(View):
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

