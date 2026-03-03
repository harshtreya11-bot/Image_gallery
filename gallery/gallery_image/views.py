from django.shortcuts import render
from .models import Product
from django.http import HttpResponse

def home(request):
    return HttpResponse("Home Page")

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

# Create your views here.
