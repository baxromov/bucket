from django.urls import path
from apps.views.home import index
from apps.views.shop import index as shop
from apps.views.blog import index as blog
from apps.views.contact import index as contact

urlpatterns = [
    path('', index, name='home'),
    path('shop', shop, name='shop'),
    path('blog', blog, name='blog'),
    path('contact', contact, name='contact'),

]
