"""geekshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from mainapp import views as mainapp

# Django 2.0
# from django.conf.urls import include
# from django.urls import re_path

# Django 3
from django.urls import path, include


urlpatterns = [
    # Django 2.0
    # re_path(r'^$', mainapp.main, name = 'main'),
    # re_path(r'^products/', include('mainapp.urls', namespace='products')),
    # re_path(r'^basket/', include('basketapp.urls', namespace='basket')),
    # re_path(r'^auth/', include('authapp.urls', namespace='auth')),
    # re_path(r'^contact/', mainapp.contact, name = 'contact'),
    # re_path(r'^admin/', include('adminapp.urls', namespace='admin')),
    # re_path(r'^control/', admin.site.urls),

    # Django 3
    path('', mainapp.main, name = 'main'),
    path('products/', include('mainapp.urls', namespace='products')),
    path('basket/', include('basketapp.urls', namespace='basket')),
    path('auth/', include('authapp.urls', namespace='auth')),
    path('contact/', mainapp.contact, name = 'contact'),
    path('admin/', include('adminapp.urls', namespace='admin')),
    path('control/', admin.site.urls),

    path('', include('social_django.urls', namespace='social'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)