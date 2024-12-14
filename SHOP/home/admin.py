
from django.contrib import admin

from home.models import Product, Color, AvailableColor, ImagesProduct


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'available']

class AvailableColorAdmin(admin.ModelAdmin):
    list_display = ['product', 'color', 'available_quantity']

# class ImageAdmin(admin.ModelAdmin):
#     list_display = ['image', 'product']



admin.site.register(Product, ProductAdmin)
admin.site.register(ImagesProduct)
admin.site.register(Color)
admin.site.register(AvailableColor,AvailableColorAdmin)
