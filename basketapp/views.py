from django.shortcuts import render, get_object_or_404
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.template.loader import render_to_string
from django.http import JsonResponse

from basketapp.models import Basket
from mainapp.models import Product

# Create your views here.

@login_required
def basket(request):
    basket_items = Basket.objects.filter(user=request.user).order_by('product__category')
    content = {
        'title': 'корзина',
        'basket_items': basket_items
    }
    return render(request, 'basketapp/basket.html', content)

@login_required
def basket_add(request, pk):
    if 'login' in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect(reverse('products:product', args=[pk]))
    # старая версия
    # product_item = get_object_or_404(Product, pk=pk)
    # basket_item = Basket.objects.filter(product=product_item, user=request.user).first()
    # if not basket_item:
    #     basket_item = Basket(user=request.user, product=product_item)
    # basket_item.quantity +=1
    # basket_item.save()
    # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    # новая версия
    product = get_object_or_404(Product, pk=pk)
    old_basket_item = Basket.get_product(user=request.user, product=product)

    if old_basket_item:
        old_basket_item[0].quantity +=1
        old_basket_item[0].save()
    else:
        new_basket_item = Basket(user=request.user, product=product)
        new_basket_item.quantity +=1
        new_basket_item.save()
        # new_basket_item.save(update_fields=['quantity', 'product']) #Странно но так не работает. Сломалась корзина
            # ValueError at /basket/add/5/
            # Cannot force an update in save() with no primary key.
            # Request Method:	GET
            # Request URL:	http://127.0.0.1:8080/basket/add/5/
            # Django Version:	3.2
            # Exception Type:	ValueError
            # Exception Value:	
            # Cannot force an update in save() with no primary key.
            # Exception Location:	D:\Nekrasov\GeekBrains\Django\Django\django_3\lib\site-packages\django\db\models\base.py, line 828, in _save_table
            # Python Executable:	D:\Nekrasov\GeekBrains\Django\Django\django_3\Scripts\python.exe



    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def basket_remove(request, pk):
    print(pk)
    basket_item = get_object_or_404(Basket, pk=pk)
    basket_item.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_edit(request, pk, quantity):
    if request.is_ajax():
        quantity = int(quantity)
        new_basket_item = Basket.objects.get(pk=pk)

        if quantity > 0:
            new_basket_item.quantity = quantity
            new_basket_item.save()
        else:
            new_basket_item.delete()
        basket_items = Basket.objects.filter(user=request.user).order_by('product__category')

        content = {
            'basket_items': basket_items
        }
        result = render_to_string('basketapp/includes/inc_basket_list.html', content)

        return JsonResponse({'result':result})
