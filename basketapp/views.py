from django.shortcuts import render, get_object_or_404
from django.shortcuts import HttpResponseRedirect

from basketapp.models import Basket
from mainapp.models import Product
# Create your views here.

def basket(request):
    pass

def basket_add(request, pk):
    product_item = get_object_or_404(Product, pk=pk)

    basket_item = Basket.objects.filter(product=product_item, user=request.user).first()

    if not basket_item:
        basket_item = Basket(user=request.user, product=product_item)
    
    basket_item.quantity +=1
    basket_item.save()
    print(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def basket_remove(request):
    pass

