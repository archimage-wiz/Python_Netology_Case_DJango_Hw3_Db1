from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones = None
    match request.GET.get('sort'):
        case None:
            phones = Phone.objects.all()
        case 'name':
            phones = Phone.objects.all().order_by('name')
        case 'max_price':
            phones = Phone.objects.all().order_by('-price')
        case 'min_price':
            phones = Phone.objects.all().order_by('price')
    context = {
        'phones': phones
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    xphone = Phone.objects.get(slug=slug)
    context = {
        'phone': xphone
    }
    return render(request, template, context)
