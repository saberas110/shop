from django.urls import path
from django.views.decorators.cache import cache_page
from home import views

app_name = 'home'

urlpatterns = [
    path('', cache_page(200)(views.HomeView.as_view()), name='home'),
    path('product/detail/<int:product_id>', views.DetailProductView.as_view(), name='detail_product'),
    path('product/comment/<int:product_id>', views.DetailProductView.as_view(), name='comment'),
    path('product/comment/like/<int:product_id>/<int:comment_id>',views.LikeCommentView.as_view(), name='like_comment'),
    path('product/comment/dislike/<int:product_id>/<int:comment_id>',views.DisLikeCommentView.as_view(), name='dislike_comment'),
    path('product/favorites/add/<int:product_id>', views.FavoritesProductView.as_view(), name='add_favorite'),
    path('product/favorites', views.FavoritesProductView.as_view(), name='favorites'),
]