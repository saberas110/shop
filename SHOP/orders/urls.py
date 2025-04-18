from django.urls import path

from orders import views

app_name = 'orders'

urlpatterns = [
    path('add/<int:product_id>', views.CartAddView.as_view(), name='add_cart'),
    path('delete/<int:product_id>/<str:color>', views.CartDeleteView.as_view(), name='delete_cart'),
    path('detail/cart', views.CartAddView.as_view(), name='detail_cart'),
    path('create', views.OrderCreateView.as_view(), name='order_create')

]