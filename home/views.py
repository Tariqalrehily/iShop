from django.shortcuts import render


def index(request):
    """To disply the index page"""
    return render(request, "index.html")
