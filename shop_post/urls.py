from django.urls import path
from shop_post import views

urlpatterns = [
    path('', views.home_page, name="home_page"),
    path('category/<int:category_pk>', views.category, name="home_page"),
    path('basket', views.basket, name="basket"),
    path('add_basket/<int:product_pk>', views.add_basket, name='add_basket'),
    path('delete_from_basket/<int:product_pk>', views.delete_from_basket, name='delete_from_basket'),
    path('basket/clear_basket', views.clear_basket, name='clear_basket'),
    
    
    
]