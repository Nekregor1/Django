from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, 'mainapp/index.html', context= {
        'title':'Главная'
    })


def products(request):
    links_menu = [
        {'href': 'products_all', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'}
    ]

    return render(request, 'mainapp/products.html',context={
        'title':'Продукты',
        'links_menu': links_menu
    })


def contact(request):
    return render(request, 'mainapp/contact.html', context= {
        'title':'Контакты'
    })


