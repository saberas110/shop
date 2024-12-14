

from home.models import Product

from django.template.defaultfilters import length

CART_SESSION_ID = 'cart'
class Cart:
    def __init__(self, request):
        self.session =  request.session
        cart = self.session.get(CART_SESSION_ID)
        if not cart:
            cart = self.session[CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        cart = self.cart.copy()
        for item in cart.values():
            product = Product.objects.get(id = item['product_id'])
            item['product'] = product
            item['total_price'] = item['quantity'] * int(item['price'])
            yield item


    def __len__(self):
        return length(self.cart.values())

    def add(self,product, quantity, color):
        product_id = str(product.id)
        if product_id not in self.cart:
            uniq_id = self.generator_uniq_id(product_id, color)
            self.cart[uniq_id] = {'quantity':0, 'price':str(product.price), 'color':color, 'product_id':product_id}
        self.cart[uniq_id]['quantity'] += quantity
        self.save()

    def delete(self, product_id, color):
        uniq_id = self.generator_uniq_id(product_id, color)
        del self.cart[uniq_id]
        self.save()


    def total_price(self):
        total_price = sum(item['total_price'] for item in self.cart.values())
        return total_price


    def generator_uniq_id(self,product_id,color):
        uniq_id = f'{product_id}-{color}'
        return uniq_id

    def save(self):
        self.session.modified = True