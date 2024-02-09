from django.contrib.auth.models import User
from django.db import models

# Modificamos el campo email después de que se ha definido el modelo User
User._meta.get_field('email')._unique = True