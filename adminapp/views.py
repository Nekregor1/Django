from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404

from authapp.models import ShopUser
from mainapp.models import Product, ProductCategory

# Create your views here.

def user_create(request):
    pass

def users(request):
    users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')
    content={
        'objects': users_list
    }
    return render(request, 'adminapp/users.html', content)

def user_update(request, pk):
    pass

def user_delete(request, pk):
    pass

def category_create(request):
    pass

def categories(request):
    categories_list = ProductCategory.objects.all().order_by('-is_active')
    content={
        'objects': categories_list
    }
    return render(request, 'adminapp/categories.html', content)

def category_update(request, pk):
    pass

def category_delete(request, pk):
    pass

def product_create(request):
    pass

def products(request, pk):
    category_item = get_object_or_404(ProductCategory, pk=pk)
    product_list = Product.objects.filter(category=category_item).order_by('-is_active')
    content={
        'objects': product_list,
        'category': category_item
    }
    return render(request, 'adminapp/products.html', content)

def product_read(request, pk):
    pass

def product_update(request, pk):
    pass

def product_delete(request, pk):
    pass 