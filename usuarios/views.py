from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UserCreationFormWithEmail
from django.contrib.auth import views as auth_views
from .forms import LoginForm
from .models import CustomUser


class SingUpView(CreateView):
    model = CustomUser
    form_class = UserCreationFormWithEmail
    template_name = 'usuarios/registro.html'
    success_url =  reverse_lazy('usuarios:login')

class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'registration/login.html'

    success_url = reverse_lazy('default_redirect_url') 

    def form_valid(self, form):
        response = super().form_valid(form)
        if 'next' in self.request.GET:
            return HttpResponseRedirect(self.request.GET['next'])
        return response
