from django.shortcuts import render, redirect

from .models import Post, Category, Basket
# Create your views here.

def home_page(request):
    post = Post.objects.all()
    category=Category.objects.all()
    return render(request, 'shop_post/home_page.html', {'post':post, 'category':category})

def category(request, category_pk):
    post = Post.objects.filter(category=category_pk)
    category = Category.objects.all()
    return render(request, 'shop_post/home_page.html', {'post':post, 'category':category})

def basket(request):
    basket = Basket.objects.filter(user = request.user).first()
    product = basket.product.all()
    return render(request, 'shop_post/basket.html', {'product':product})

def add_basket(request, product_pk):
    product = Post.objects.get(pk = product_pk)
    basket = Basket.objects.filter(user = request.user).first()
    if basket==None:
        basket = Basket.objects.create(user = request.user)
        quantity = 1
    else:
        basket.product.add(product)
        quantity += 1
    return redirect('basket')

def delete_from_basket(request, product_pk):
    basket = Basket.objects.filter(user = request.user).first()
    product = basket.product.remove(product_pk)
    return redirect('basket')

def clear_basket(request):
    basket = Basket.objects.filter(user = request.user).first()
    basket.product.clear()
    return redirect('basket')

