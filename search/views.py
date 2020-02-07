from django.shortcuts import render
from products.models import Product


def do_search(request):
    """
    filter search by name, brand and year
    """
    products = Product.objects.filter(name__icontains=request.GET['q'])
    return render(request, "search_results.html", {"products": products})
    

def filter(request):
    product = Product.objects.filter(brand__icontains=request.GET['brand']).filter(year__icontains=request.GET['year'])
    return render(request, "search_results.html", {"products": product})