from django.urls import path
from mainapp import views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.products, name = 'products'),
    path('<int:pk>/', mainapp.products, name = 'category'),
    path('product/<int:pk>/', mainapp.product, name='product')
]
