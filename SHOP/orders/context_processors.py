from .cart import Cart
def cart(request):
    cart_session = Cart(request)
    uniq_id = []
    for key in  cart_session.cart.keys():
        uniq_id.append(key)
    return {
        'cart': cart_session,
        'uniq_id': uniq_id
    }