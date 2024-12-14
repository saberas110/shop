from django.core.exceptions import ValidationError
from django.db import models
from django.utils.text import slugify


class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True,null=True, blank=True)
    description = models.TextField()
    price = models.IntegerField()
    available = models.BooleanField(default=True)
    color = models.ManyToManyField('Color',null=True, blank=True )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    
    



    class Meta:
        ordering = ['name']


    def __str__(self):
        return self.name
    
    def save(self,*args):
        self.slug = slugify(self.name)
        super().save(*args)

class Color(models.Model):
    name = models.CharField(max_length=50)
    color_code = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class AvailableColor(models.Model):
    color = models.ForeignKey(Color, on_delete=models.CASCADE, related_name='availables')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='availables')
    available_quantity = models.PositiveIntegerField()
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ['available_quantity']

    def __str__(self):
        return self.product.name
    
    def save(self, *args):
        if self.available_quantity == 0 :
            self.available = False
        # if AvailableColor.objects.filter(color__name=self.color.name, product__slug=self.product.slug).exists():
        #     raise ValidationError('This color already exist')
        super().save( *args)



class ImagesProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='media/product')
    def __str__(self):
        return self.product.slug

