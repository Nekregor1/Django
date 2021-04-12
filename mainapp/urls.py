from mainapp import views as mainapp
# Django 2.0
# from django.urls import re_path

# Django 3
from django.urls import path


app_name = 'mainapp'

urlpatterns = [
    # Django 2.0
    # re_path(r'^$', mainapp.products, name = 'products'),
    # re_path(r'category/(?P<pk>\d+)/$', mainapp.products, name = 'category'),
    # # path('category/<int:pk>/<int:page>', mainapp.products, name = 'page'),
    # re_path(r'product/(?P<pk>\d+)/$', mainapp.product, name='product')

    # Django 3
    path('', mainapp.products, name = 'products'),
    path('category/<int:pk>/', mainapp.products, name = 'category'),
    # path('category/<int:pk>/<int:page>', mainapp.products, name = 'page'),
    path('product/<int:pk>/', mainapp.product, name='product')
]
