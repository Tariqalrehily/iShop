from django.shortcuts import render
from .models import Product


# Create products views here.
def all_products(request):
    products = Product.objects.all()[:6]
    return render(request, "products.html", {"products": products})


def description(request):
    description = Product.objects.all()
    return render(request, "description.html", {"description": description})
