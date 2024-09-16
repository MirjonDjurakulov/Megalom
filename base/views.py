from email.policy import default

from django.shortcuts import render
from unicodedata import category

from .models import Categories, Products

def index(request, slug='chyornyj-metall'):
    categories = Categories.objects.all()
    category_filter = Categories.objects.get(slug=slug)
    products = Products.objects.filter(category=category_filter)

    context = {
        'categories': categories,
        'products': products,
    }

    return render(request, 'index.html' , context)
# Create your views here.
