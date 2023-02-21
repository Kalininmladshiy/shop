from django.urls import path
from .views import product_list, product_detail, order_create

urlpatterns = [
    path('', product_list, name='product_list'),
    path('<slug:category_slug>', product_list, name='product_list_by_category'),
    path('products/<slug:slug>', product_detail, name='product_detail'),
    path('orders/', order_create, name='order_create'),
]
