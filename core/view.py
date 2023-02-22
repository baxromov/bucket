from django.shortcuts import render

def home(request):
    return render(request, 'temp/blog.html')

def index(request):
    return render(request, 'temp/index.html')

def shop_grid(request):
    return render(request, 'temp/shop-grid.html')

def blog(request):
    return render(request, 'temp/blog.html')

def contact(request):
    return render(request, 'temp/contact.html')

def blog_details(request):
    return render(request, 'temp/blog-details.html')

def checkout(request):
    return render(request, 'temp/checkout.html')

def shop_details(request):
    return render(request, 'temp/shop-details.html')

def shoping_cart(request):
    return render(request, 'temp/shoping-cart.html')

