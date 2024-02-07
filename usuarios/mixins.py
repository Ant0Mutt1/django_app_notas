from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import AccessMixin


class CustomLoginRequiredMixin(AccessMixin):
    @method_decorator(login_required(login_url='/usuario/login/'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
