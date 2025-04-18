from syslog import LOG_INFO
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template.defaultfilters import length
from orders.cart import Cart
from django.shortcuts import render,get_object_or_404, redirect
from django.views import View
from .models import Product, Comment, LikeDislikeComment,FavoriteProduct
from .forms import CommentForm
from django.contrib import messages



class HomeView(View):

    def get(self, request):
        return render(request, 'home/home.html')

class DetailProductView(LoginRequiredMixin,View):
    form_class = CommentForm
    def setup(self, request, *args, **kwargs):
        self.product_id = kwargs['product_id']
        self.product = get_object_or_404(Product, id=self.product_id)
        return super().setup(args, kwargs)

    def get(self,request, **kwargs):
        is_favorite = False
        is_cart = False
        cart = Cart(request)
        colors = self.product.availables.all()
        last_color = colors.last().color
        comments = self.product.comments.all()
        if FavoriteProduct.objects.filter(product_id=self.product_id, user_id=request.user.id).exists():
            is_favorite = True
        if request.session.get('cart'):
            if request.session.get('cart').get(cart.generator_uniq_id(self.product_id, last_color)):
                is_cart = True
        return render(request, 'home/detail_product.html',
                      {'product':self.product,'colors':colors,'is_cart':is_cart,
                       'form':self.form_class,'comments':comments, 'is_favorite':is_favorite})

    def post(self,request,**kwargs):
        form = self.form_class(request.POST)
        star = request.POST.get('rating')
        if form.is_valid():
            cd = form.cleaned_data
            Comment.objects.create(text=cd['text'], user=request.user, product=self.product,star=star,
                                   positive_point=cd['positive_point'],negative_point=cd['negative_point'] )
            messages.success(request, 'نظر شما با موفقیت ثبت شد', 'success')
            return redirect('home:detail_product' ,self.product_id)
        messages.error(request,'فرم معتبر نمیباشد', 'danger')
        return redirect('home:detail_product', self.product_id)


class LikeCommentView(LoginRequiredMixin,View):
    def get(self,request, product_id, comment_id):

        try:
            like = LikeDislikeComment.objects.get(comment_id=comment_id, user_id=request.user.id, like=True)
            like.delete()
        except LikeDislikeComment.DoesNotExist :
            try:
                like = LikeDislikeComment.objects.get(comment_id=comment_id, user_id=request.user.id, dislike=True)
                like.dislike = False
                like.like = True
                like.save()
            except LikeDislikeComment.DoesNotExist:
                LikeDislikeComment.objects.create(comment_id=comment_id, user_id=request.user.id, like=True)

        return redirect('home:detail_product',product_id)


class DisLikeCommentView(LoginRequiredMixin,View):
    def get(self,request, product_id, comment_id):

        try:
            dislike = LikeDislikeComment.objects.get(comment_id=comment_id, user_id=request.user.id, dislike=True)
            dislike.delete()
        except LikeDislikeComment.DoesNotExist :
            try:
                dislike = LikeDislikeComment.objects.get(comment_id=comment_id, user_id=request.user.id, like=True)
                dislike.like = False
                dislike.dislike = True
                dislike.save()
            except LikeDislikeComment.DoesNotExist:
                LikeDislikeComment.objects.create(comment_id=comment_id, user_id=request.user.id, dislike=True)
        return redirect('home:detail_product',  product_id)



class FavoritesProductView(LoginRequiredMixin,View):
    def get(self, request, product_id=None):
        if product_id:
            try:
                favorite=FavoriteProduct.objects.get(product_id=product_id, user=request.user)
                print('fav', favorite)
                favorite.delete()
                return redirect('home:favorites')
            except FavoriteProduct.DoesNotExist:
                FavoriteProduct.objects.create(product_id=product_id, user_id=request.user.id)
                return redirect('home:favorites')

        else:
            favorites=FavoriteProduct.objects.all()
            return render(request, 'home/favorites.html', {'favorites':favorites,
                                                           'is_active_favorites':'active'})






