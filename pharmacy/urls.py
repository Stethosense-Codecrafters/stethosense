from . import views
from django.urls import path
from django.contrib.auth import views as authentication_views

app_name = 'pharmacy'
from . import views

urlpatterns = [
    path('pharmacy_home/', views.pharmacy_home, name='pharmacy_home'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('pharmacy_contact/', views.pharmacy_contact, name='pharmacy_contact'),
    path('pharmacy_about/', views.pharmacy_about, name='pharmacy_about'),
    path('shop_single/', views.shop_single, name='shop_single'),
    path('shop/', views.shop, name='shop'),
    path('upload_prescription/', views.upload_prescription, name='upload_prescription'),
    path('order_medicine/', views.order_medicine, name='order_medicine'),
    path('view_cart/', views.view_cart, name='view_cart'),
    path('track_order/<int:order_id>/', views.track_order, name='track_order'),
]
