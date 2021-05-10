from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.conf import settings
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt


from authapp.models import ShopUser
from authapp.forms import ShopUserLoginForm, ShopUserRegisterForm, ShopUserEditForm, ShopUserProfileEditForm
# Create your views here.

# @csrf_exempt
def login(request):
    title = 'вход'

    login_form = ShopUserLoginForm(data=request.POST)

    # next = request.GET.get('next', '')
    next = request.GET['next'] if 'next' in request.GET else ''

    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            if 'next' in request.POST:
                return HttpResponseRedirect(request.POST['next'])
            return HttpResponseRedirect(reverse('main'))

    content = {
        'title': title,
        'login_form': login_form,
        'next': next
    }
    return render(request, 'authapp/login.html', content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))


def register(request):

    if request.method == 'POST':
        register_form = ShopUserRegisterForm(request.POST, request.FILES)
        if register_form.is_valid():
            user = register_form.save()
            if send_verify_email(user):
                print('success')
            else:
                print('failed')
            
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        register_form = ShopUserRegisterForm()
    
    content = {
        'title': 'регистрация',
        'form': register_form
    }
    return render(request, 'authapp/register.html', content)

def edit(request):
    if request.method == 'POST':
        edit_form = ShopUserEditForm(request.POST, request.FILES, instance=request.user)
        profile_form = ShopUserProfileEditForm(request.POST, instance=request.user.shopuserprofile)
        if edit_form.is_valid() and profile_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('auth:edit'))
    else:
        edit_form = ShopUserEditForm(instance=request.user)
        profile_form = ShopUserProfileEditForm(instance=request.user.shopuserprofile)

    content = {
        'title': 'редактирование',
        'edit_form': edit_form,
        'profile_form': profile_form
    }

    return render(request, 'authapp/edit.html', content)


def send_verify_email(user):
    verify_link = reverse('auth:verify', args=[user.email, user.activation_key])

    subject = f'Подтверждение учетной записи {user.email}'

    message = f'Ссылка для активации: {settings.BASE_URL}{verify_link}'

    return send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=True)

def verify(request, email, activation_key):
    user = ShopUser.objects.get(email=email)
    if user.activation_key == activation_key and not user.is_activation_key_expired():
        user.is_active = True
        user.activation_key = ''
        user.save()
        auth.login(request, user)
    return render(request, 'authapp/verification.html')