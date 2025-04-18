from django.contrib import admin
from .models import OrderItem, Order


class OrderItem(admin.TabularInline):
    model = OrderItem

@admin.register(Order)
class Order(admin.ModelAdmin):
    list_display = ['id', 'user', 'updated', 'paid']
    list_filter = ['paid']
    inlines = [OrderItem]
