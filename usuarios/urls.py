from django.urls import path
from .views import SingUpView
from .views import LoginView


app_name = 'usuarios'

urlpatterns = [
    path('', SingUpView.as_view(), name='registro'),
    path('login/', LoginView.as_view(), name='login'),
]

