from django.contrib.auth import views as auth_views
from django.contrib.auth import get_user_model
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from .forms import LoginForm
from .forms import UserCreationFormWithEmail


class SingUpView(CreateView):
    model = get_user_model()
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
    
class DeleteUser(SuccessMessageMixin, DeleteView):
    model = get_user_model()
    template_name = 'usuarios/eliminar_cuenta_confirmacion.html'
    success_url = reverse_lazy('usuarios:login')
    success_message = 'Tu cuenta fue eliminada de Otra App de Notas'

