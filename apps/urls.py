from django.urls import path
from apps.views.home import index

urlpatterns = [
    path('index/', index)
]
