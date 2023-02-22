from django.shortcuts import render

def home(request):
    return render(request, 'blog.html')

def index(request):
    return render(request, 'index.html')

def shop_grid(request):
    return render(request, 'shop-grid.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')

def blog_details(request):
    return render(request, 'blog-details.html')

def checkout(request):
    return render(request, 'checkout.html')

def shop_details(request):
    return render(request, 'shop-details.html')

def shoping_cart(request):
    return render(request, 'shoping-cart.html')

