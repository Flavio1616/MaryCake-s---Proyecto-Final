from django.shortcuts import render
from .models import Torta
from .models import Postres

# Create your views here.
def torta(request):
    torta = Torta.objects.all()
    return render(request, "productos/torta.html", {'torta': torta})

def postre(request):
    postre = Postres.objects.all()
    return render(request, "productos/postre.html", {'postre': postre})