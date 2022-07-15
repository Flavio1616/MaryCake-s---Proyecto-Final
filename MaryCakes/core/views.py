from django.shortcuts import HttpResponse, render

html_base = """
    "<h1>MARY CAKES</h1>
    <ul>
        <li><a href="/">PORTADA</a></li>
        <li><a href="/torta/">TORTAS</a></li>
        <li><a href="/postre/">POSTRES Y BOCADITOS</a></li>
        <li><a href="/about/">SOBRE NOSOTROS</a></li>
        <li><a href="/contact/">CONTACTO</a></li>
    </ul>
"""

# Create your views here.
def home(request):
    return render(request, "core/home.html")

def torta(request):
    return render(request, "core/torta.html")

def postre(request):
    return render(request, "core/postre.html")

def about(request):
    return render(request, "core/about.html")

def contact(request):
    return render(request, "core/contact.html")
