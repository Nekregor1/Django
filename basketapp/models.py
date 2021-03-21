from django.conf import settings
from django.db import models

from mainapp.models import Product

# Create your models here.

class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='basket')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(verbose_name='количество', default=0)
    add_datetime = models.DateTimeField(auto_now_add=True, verbose_name='время')
