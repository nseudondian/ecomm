from django.shortcuts import render
from .models import Item

def home(request):
    context = {
        'items':Item.objects.all()
    }
    return render(request, 'mainapp/home-page.html', context)

def product(request):
    context = {
        'items':Item.objects.all()
    }
    return render(request, 'mainapp/product-page.html', context)
