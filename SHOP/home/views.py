from django.template.defaultfilters import length

from orders.cart import Cart
from django.shortcuts import render,get_object_or_404
from django.views import View
from .models import Product


class HomeView(View):
    def get(self, request):
        return render(request, 'home/home.html')

class DetailProductView(View):
    def get(self,request, product_id):
        cart = Cart(request)
        print('values', cart.cart.values())
        is_cart = False
        product = get_object_or_404(Product, id=product_id)
        colors = product.availables.all()
        last_color = colors.last().color
        if request.session.get('cart'):
            if request.session.get('cart').get(cart.generator_uniq_id(product_id, last_color)):
                is_cart = True
        return render(request, 'home/detail_product.html',
                      {'product':product,'colors':colors,'is_cart':is_cart})

