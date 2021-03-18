from django.shortcuts import render

# Create your views here.


def login(request):
    
    content = {
        'title': 'вход',
    }
    return render(request, 'authapp/login.html', content)


def logout(request):
    pass