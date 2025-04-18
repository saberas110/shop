from django.urls import path

from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('register', views.UserRegisterView.as_view(), name='register'),
    path('otp', views.OtpRegisterView.as_view(), name='otp'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('profile', views.EditProfileView.as_view(), name='edit_profile'),
    path('password', views.SetOrChangePasswordView.as_view(), name='change_password'),
    path('address', views.AddressView.as_view(), name='address_list'),
    path('address/add', views.AddressAddView.as_view(), name='add_address'),
]