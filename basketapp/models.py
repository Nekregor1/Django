from django.conf import settings
from django.db import models

from mainapp.models import Product

# Create your models here.

# class BasketQuerySet(models.QuerySet):
#     def delete(self):
#         for item in self:
#             # Может все таки минус, чтобы количество вычеталось из остатков?
#             item.product.quantity -= item.quantity
#             item.product.save()
#         super().delete()


class Basket(models.Model):
    # objects = BasketQuerySet.as_manager()
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='basket')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(verbose_name='количество', default=0)
    add_datetime = models.DateTimeField(auto_now_add=True, verbose_name='время')

    @property
    def product_cost(self):
        return self.product.price * self.quantity

    @property
    def total_quantity(self):
        _items = Basket.objects.filter(user=self.user)
        _total_quantity = sum(list(map(lambda x: x.quantity, _items)))
        return _total_quantity

    @property
    def total_cost(self):
        _items = Basket.objects.filter(user=self.user)
        _total_cost = sum(list(map(lambda x: x.product_cost, _items)))
        return _total_cost

    @staticmethod
    def get_items(user):
        return Basket.objects.filter(user=user).order_by('product__category')

    @staticmethod
    def get_product(user, product):
        return Basket.objects.filter(user=user, product=product)

    @classmethod
    def get_products_quantity(cls, user):
        basket_items = cls.get_items(user)
        basket_items_dic = {}
        [basket_items_dic.update({item.product: item.quantity}) for item in basket_items]

        return basket_items_dic

    @staticmethod
    def get_item(pk):
        return Basket.objects.get(pk=pk)


    # def delete(self):
    #     # Может все таки минус, чтобы количество вычеталось из остатков?
    #     self.product.quantity += self.quantity
    #     self.product.save()
    #     super().delete()