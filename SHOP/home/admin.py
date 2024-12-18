
from django.contrib import admin

from home.models import Product, Color, AvailableColor, ImagesProduct, Comment, LikeDislikeComment


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'available']

class AvailableColorAdmin(admin.ModelAdmin):
    list_display = ['product', 'color', 'available_quantity']

# class ImageAdmin(admin.ModelAdmin):
#     list_display = ['image', 'product']

class LikeDislikeAdmin(admin.ModelAdmin):
    list_display = ['comment', 'user']


admin.site.register(Product, ProductAdmin)
admin.site.register(LikeDislikeComment, LikeDislikeAdmin)
admin.site.register(ImagesProduct)
admin.site.register(Color)
admin.site.register(Comment)
admin.site.register(AvailableColor,AvailableColorAdmin)
