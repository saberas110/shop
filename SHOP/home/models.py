from email.policy import default
from html.entities import html5

from django.core.exceptions import ValidationError
from django.db import models
from django.template.defaultfilters import length
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator

from accounts.models import User


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



class FavoriteProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='favorites')

    def __str__(self):
        return f'{self.product.name}-{self.user.phone_number}'




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


class Comment(models.Model):
    text = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    star = models.PositiveIntegerField(max_length=1, validators=(MinValueValidator(0), MaxValueValidator(5)))
    positive_point = models.CharField(max_length=100)
    negative_point = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True,null=True, blank=True)

    def get_avrage_star(self):
        result = sum( item.star for item in Comment.objects.all())
        result = result/length(Comment.objects.all())
        return result

    def get_star(self):
        avrage_star = self.get_avrage_star()
        if avrage_star % int(avrage_star) == 0:
            avrage_star = int(avrage_star)
        if isinstance(avrage_star, int):
            for star in range(5-avrage_star):
                yield 'bi bi-star'
            for star in range(int(avrage_star)):
                yield 'bi bi-star-fill'
        else:
            for star in range(5-(int(avrage_star+1))):
                yield 'bi bi-star'
            yield 'bi bi-star-half'
            for star in range(int(avrage_star)):
                yield 'bi bi-star-fill'



    def __str__(self):
        return self.text[:20]


class LikeDislikeComment(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    like = models.BooleanField(default=False)
    dislike = models.BooleanField(default=False)








