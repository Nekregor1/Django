from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from adminapp.forms import ProductEditForm
from adminapp.forms import ShopUserAdminEditForm
from authapp.forms import ShopUserRegisterForm
from authapp.models import ShopUser
from mainapp.models import Product, ProductCategory
from django.contrib.auth.decorators import user_passes_test

# Create your views here.

@user_passes_test(lambda u: u.is_superuser)
def user_create(request):
    if request.method == 'POST':
        user_form = ShopUserRegisterForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('admin:user_read'))
    else:
        user_form = ShopUserRegisterForm()
    content = {
        'form': user_form
    }

    return render(request, 'adminapp/user_update.html', content)

@user_passes_test(lambda u: u.is_superuser)
def users(request):
    users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')
    content={
        'objects': users_list
    }
    return render(request, 'adminapp/users.html', content)

@user_passes_test(lambda u: u.is_superuser)
def user_update(request, pk):
    edit_user = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        user_form = ShopUserAdminEditForm(request.POST, request.FILES, instance=edit_user)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('admin:user_read'))
    else:
        user_form = ShopUserAdminEditForm(instance=edit_user)

    content = {
        'form': user_form
    }
    return render(request, 'adminapp/user_update.html', content)

@user_passes_test(lambda u: u.is_superuser)
def user_delete(request, pk):
    user_item = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        if user_item.is_active:
            user_item.is_active = False
        else:
            user_item.is_active = True
        user_item.save()
        return HttpResponseRedirect(reverse('admin:user_read'))
    
    content = {
        'user_to_delete': user_item
    }
    return render(request, 'adminapp/user_delete.html', content)

@user_passes_test(lambda u: u.is_superuser)
def category_create(request):
    pass

@user_passes_test(lambda u: u.is_superuser)
def categories(request):
    categories_list = ProductCategory.objects.all().order_by('-is_active')
    content={
        'objects': categories_list
    }
    return render(request, 'adminapp/categories.html', content)

@user_passes_test(lambda u: u.is_superuser)
def category_update(request, pk):
    pass

@user_passes_test(lambda u: u.is_superuser)
def category_delete(request, pk):
    pass

@user_passes_test(lambda u: u.is_superuser)
def product_create(request):
    pass

@user_passes_test(lambda u: u.is_superuser)
def products(request, pk):
    category_item = get_object_or_404(ProductCategory, pk=pk)
    product_list = Product.objects.filter(category=category_item).order_by('-is_active')
    content={
        'objects': product_list,
        'category': category_item
    }
    return render(request, 'adminapp/products.html', content)

@user_passes_test(lambda u: u.is_superuser)
def product_read(request, pk):
    pass

@user_passes_test(lambda u: u.is_superuser)
def product_update(request, pk):
    edit_product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        update_form = ProductEditForm(request.POST, request.FILES, instance=edit_product)
        if update_form.is_valid():
            update_form.save()
            return HttpResponseRedirect(reverse('admin:products', args=[edit_product.category_id]))
    else:
        update_form = ProductEditForm(instance=edit_product)

    content ={
        'form': update_form,
        'category': edit_product.category,
    }
    return render(request, 'adminapp/product_update.html', content)

@user_passes_test(lambda u: u.is_superuser)
def product_delete(request, pk):
    pass 