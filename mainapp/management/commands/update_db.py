from django.core.management import BaseCommand

from authapp.models import ShopUser, ShopUserProfile

class Command(BaseCommand):
    def handle(self, *args, **options):
        users = ShopUser.objects.all()
        for user in users:
            users_profile = ShopUserProfile.objects.create(user=user)
            users_profile.save()
            
