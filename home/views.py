from django.shortcuts import render

# Create your views here.
def index(request):
    """To disply the index page"""
    return render(request, "index.html")
