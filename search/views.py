from django.shortcuts import render
from products.models import Product


def do_search(request):
    """
    filter search by name
    """
    products = Product.objects.filter(name__icontains=request.GET['q'])
    return render(request, "search_results.html", {"products": products})
    

def filter(request):
    """
    filter search by name, brand and year
    """
    product = Product.objects.filter(name__icontains=request.GET['q']).filter(brand__icontains=request.GET['brand']).filter(year__icontains=request.GET['year'])
    return render(request, "search_results.html", {"products": product})