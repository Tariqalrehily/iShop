from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator, EmptyPage, InvalidPage


def products(request):
    products = Product.objects.all()[:6]
    return render(request, "products.html", {"products": products})


def more_products(request):
    """
    Products list to disply 9 in each page
    Credit to : GoDjango
    """
    products = Product.objects.all()

    paginater = Paginator(products, 9)

    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1

    try:
        products = paginater.page(page)
    except(EmptyPage, InvalidPage):
        products = paginater.page(paginater.num_pages)

    context = {'products': products}
    return render(request, 'more_products.html', context)


def product_view(request, slug):
    product = Product.objects.get(slug=slug)
    return render(request, "product_view.html", {"product": product})

