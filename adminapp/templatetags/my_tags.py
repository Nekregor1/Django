from django.conf import settings
from django import template

register = template.Library()

@register.filter(name='media_for_users')
def media_for_users(path_to_avatar):
    if not path_to_avatar:
        path_to_avatar = "users_avatars/user1.jpg"  
    return f'{settings.MEDIA_URL}{path_to_avatar}'


def media_for_products(path_to_image):
    if not path_to_image:
        path_to_image = "products_images/default.jpg"
    return f'{settings.MEDIA_URL}{path_to_image}'

register.filter('media_for_products', media_for_products)