from django.shortcuts import render
from phones.models import Phone


def show_catalog(request):
    sort = request.GET.get('sort', 'name')
    template = 'catalog.html'
    dic = {}
    phones = {'name': Phone.objects.all().order_by("name"),
              'min_price': Phone.objects.all().order_by("price"),
              'max_price': Phone.objects.all().order_by("-price")
              }
    context = {
        'phones': phones[sort]
    }
    print(phones)
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phones = Phone.objects.get(slug=slug)
    context = {'phones': phones}
    return render(request, template, context)
