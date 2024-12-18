from django import template
from django.template.defaultfilters import length
from home.models import Product

register = template.Library()

@register.filter
def is_like(likes,request):
    liked = False
    for item in likes.filter(like=True).values():
        if item['user_id'] == request.user.id:
            liked = True
            break

    return liked

@register.filter
def is_dislike(likes,request):
    dis_liked = False

    for item in likes.filter(dislike=True).values():
        if item['user_id'] == request.user.id:
            dis_liked = True

            break
    return dis_liked


@register.filter
def length_like(likes):
    return length(likes.filter(like=True))


@register.filter
def length_dislike(likes):
    return length(likes.filter(dislike=True))

@register.filter
def length_star(product_id,number_star):
    return length(Product.objects.get(id = product_id).comments.filter(star=number_star))

@register.filter
def percentage_star(product_id,number_star):
    product_comment = Product.objects.get(id=product_id).comments
    length_star_number=length(product_comment.filter(star=number_star))
    length_all_star = length(product_comment.all())
    print('le',length_star_number)
    return int(length_star_number/length_all_star *100)


