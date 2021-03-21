import datetime
import os
import json

from django.conf import settings
from django.shortcuts import render, get_object_or_404

from mainapp.models import Product, ProductCategory
from basketapp.models import Basket

# Create your views here.

def main(request):
    title = 'главная'
    products = Product.objects.all()[:4]
    context = {'title': title, 'products': products}
    return render(request, 'mainapp/index.html', context)


def products(request, pk=None):
    basket = 0
    if request.user.is_authenticated:
        basket = sum(list(Basket.objects.filter(user=request.user).values_list('quantity', flat=True)))

    title = 'Продукты'
    links_menu = ProductCategory.objects.all()
    if pk is not None:
        if pk == 0:
            products_list = Product.objects.all().order_by('price')
            category_item = {'name':'все','pk':0}
        else:
            category_item = get_object_or_404(ProductCategory, pk=pk)
            products_list = Product.objects.filter(category=category_item)

        context = {
            'title': title,
            'links_menu': links_menu,
            'category': category_item,
            'products': products_list,
            'basket': basket
        }
        return render(request, 'mainapp/products_list.html', context)

    same_products = Product.objects.all()[:4]
    context={
        'title': title,
        'links_menu': links_menu,
        'same_products': same_products,
        'basket': basket
    }

    return render(request, 'mainapp/products.html',context)



def contact(request):
    title = 'О нас'
    locations = []

    with open(os.path.join(settings.BASE_DIR, f'mainapp/json/contact_locations.json'), encoding='utf-8') as f:
        locations = json.load(f)
    context = {'title':title, 'locations': locations}

    return render(request, 'mainapp/contact.html', context)


