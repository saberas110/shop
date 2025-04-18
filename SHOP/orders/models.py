from django.core.validators import MinValueValidator,MaxValueValidator
from django.db import models
from home.models import Product
from django.contrib.auth import get_user_model

class Order(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='orders')
    paid = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    discount = models.PositiveIntegerField(default=None, null=True, blank=True)

    def total_price(self):
        if self.discount:
            return sum(item.get_cost() for item in self.items.all()) * (1-self.discount/100)
        else:
            return sum(item.get_cost() for item in self.items.all())

    def __str__(self):
        return f'{self.user} - {self.id}'



class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField(default=1)
    color = models.CharField(max_length=20)

    def get_cost(self):
        return self.quantity * self.price
    def __str__(self):
        return f'{self.order.user.fullname} - {self.product.name}'



class Coupon(models.Model):
    code = models.CharField(max_length=30, unique=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(90)])
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.code