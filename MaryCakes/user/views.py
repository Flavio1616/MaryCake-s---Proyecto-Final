from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib import messages
from django.views import View
from django.contrib.auth.views import LoginView
# Create your views here.
def register(request):
    if request.method =='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, "user/register.html",{'formulario': form})

class CustomLoginView(LoginView):
    form_class = loginForm
    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')
        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)
            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True
        # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(CustomLoginView, self).form_valid(form)

