from django.urls import path
from gallery_image import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('product_list/', views.product_list, name='product_list'),
]