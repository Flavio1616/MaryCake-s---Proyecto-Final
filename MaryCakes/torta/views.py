from django.shortcuts import render
from .models import Torta

# Create your views here.
def torta(request):
    tortas = Torta.objects.all()
    return render(request, "torta/torta.html", {'tortas' : tortas})
