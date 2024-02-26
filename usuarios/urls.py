from django.urls import path
from .views import SingUpView
from .views import LoginView
from .views import DeleteUser


app_name = 'usuarios'

urlpatterns = [
    path('', SingUpView.as_view(), name='registro'),
    path('login/', LoginView.as_view(), name='login'),
    path('borrar_cuenta/<int:pk>', DeleteUser.as_view(), name='delete')
]

