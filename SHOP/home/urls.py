from django.urls import path

from home import views

app_name = 'home'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('product/detail/<int:product_id>', views.DetailProductView.as_view(), name='detail_product')
]