import datetime
import os
import json

from django.conf import settings
from django.shortcuts import render

from mainapp.models import Product, ProductCategory

# Create your views here.

def main(request):
    title = 'главная'
    products = Product.objects.all()[:4]
    context = {'title': title, 'products': products}
    return render(request, 'mainapp/index.html', context)


def products(request, pk=None):
    title = 'Продукты'
    same_products = Product.objects.all()[:4]
    links_menu = ProductCategory.objects.all()
    context={
        'title': title,
        'links_menu': links_menu,
        'same_products': same_products
    }
    return render(request, 'mainapp/products.html',context)


def contact(request):
    title = 'О нас'
    locations = []
    with open(os.path.join(settings.BASE_DIR, 'contacts.json'), encoding='utf-8') as f:
        locations = json.load(f)
    context = {'title':title, 'locations': locations}
    return render(request, 'mainapp/contact.html', context)


