# from typing import OrderedDict
# from urllib.parse import urlunparse, urlencode

import requests
from authapp.models import ShopUserProfile, ShopUser
import datetime 

def save_user_profile(backend, user, response, *args, **kwargs):
    if backend.name != 'vk-oauth2':
        return
    
    api_url = f"https://api.vk.com/method/users.get?fields=bdate,sex,about,city,photo_max&access_token={response['access_token']}&v=5.92"
    # api_url = urlunparse(('https',
    #                       'api.vk.com',
    #                       '/method/users.get',
    #                       None,
    #                       urlencode(OrderedDict(fields=','.join(('bdate', 'sex', 'about')),
    #                       access_token=response['access_token'],
    #                                             v='5.92')),
    #                       None
    #                       ))

    resp = requests.get(api_url)
    if resp.status_code != 200:
        return

    print(resp.json())
    data = resp.json()['response'][0]

    if data['sex']:
        if data['sex'] == 1:
            user.shopuserprofile.gender = ShopUserProfile.FEMALE
        elif data['sex'] == 2:
            user.shopuserprofile.gender = ShopUserProfile.MALE


    if data['about']:
        user.shopuserprofile.about_me = data['about']

    if data['bdate']:
        bdate = datetime.datetime.strptime(data['bdate'], '%d.%m.%Y').date()
        age = datetime.datetime.now().date().year - bdate.year
        print(age)
        user.age = age
        if age < 18:
            user.delete()
            raise AuthForbidden('social_core.backends.vk.VKOAuth2')


    if data['photo_max']:
        photo = requests.get(data['photo_max'])
        if photo.status_code == 200:
            photo_name = f'/users_avatars/{user.pk}.jpg'
            with open(f'media/{photo_name}', 'wb') as avatar:
                avatar.write(photo.content)
                user.avatar = photo_name

    user.save()

