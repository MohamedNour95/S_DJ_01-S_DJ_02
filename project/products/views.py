from django.shortcuts import render
from .models import Product
# Create your views here.
def product(request):
    return render(request, 'product.html')

def products(request):
    return render(request, 'products.html' , {'pro':Product.objects.all()})    