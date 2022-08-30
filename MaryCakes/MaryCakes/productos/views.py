from turtle import title
from urllib import request
from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from .models import Torta
from .models import Postres

# Create your views here.
def torta(request):
    torta = Torta.objects.all()
    return render(request, "productos/torta.html", {'torta': torta})

def postre(request):
    postre = Postres.objects.all()
    return render(request, "productos/postre.html", {'postre': postre})

class detailTor (View):
    def get(self, request, slug, *args, **Kwagrs):
        torta = get_object_or_404(Torta, slug=slug)
        return render(request, 'productos/detaileTorta.html', {'torta': torta})

class detailPost (View):
    def get(self, request, slug, *args, **Kwagrs):
        postre = get_object_or_404(Postres, slug=slug)
        return render(request, 'productos/detailePost.html', {'postre': postre})

class detailCart (View):
    def get(self, request, slug, *args, **Kwagrs):
        postre = get_object_or_404(Postres, slug=slug)
        return render(request, 'productos/compra.html', {'postre': postre})

class detailCart2 (View):
    def get(self, request, slug, *args, **Kwagrs):
        torta = get_object_or_404(Torta, slug=slug)
        return render(request, 'productos/compra2.html', {'torta': torta})
