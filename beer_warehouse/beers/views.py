from django.shortcuts import render
from django.http import HttpResponse
from beers.models import Cuento

def  first_view(request):
    context = {
        'otra_cosa': [1, 2, 3]
    }
    return render(request, 'beers.html', context)


def  beer_list_view(request):
    context = {
        'cuentos': Cuento.objects.all().order_by("title")[:4]
    }
    return render(request, 'beer_list_view.html', context)

def all_beers_list_view(request):
    context = {
        'cuentos': Cuento.objects.all().order_by("title")
    }
    return render(request, 'all_beers_list.html', context)

def beer_detail_view(request, id, *args, **kwargs):
    context = {
        'cuento': Cuento.objects.get(id=id)
    }
    return render(request, 'beer_detail_view.html', context)
