from django.shortcuts import render
from .models import Product


def all_products(request):
    products = Product.objects.all()[:6]
    return render(request, "products.html", {"products": products})


def more_products(request):
    products = Product.objects.all()
    return render(request, "more_products.html", {"products": products})
