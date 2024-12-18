from django.urls import path

from home import views

app_name = 'home'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('product/detail/<int:product_id>', views.DetailProductView.as_view(), name='detail_product'),
    path('product/comment/<int:product_id>', views.DetailProductView.as_view(), name='comment'),
    path('product/comment/like/<int:product_id>/<int:comment_id>',views.LikeCommentView.as_view(), name='like_comment'),
    path('product/comment/dislike/<int:product_id>/<int:comment_id>',views.DisLikeCommentView.as_view(), name='dislike_comment'),
]