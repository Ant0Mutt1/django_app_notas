from django.contrib.auth.models import User
from usuarios.models import CustomUser
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Etiqueta(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, default='')

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):

        self.slug = slugify(self.nombre)
        super(Etiqueta, self).save()   

    def get_update_url(self):
        return reverse('notas:modificar_etiqueta', args=[self.pk])

    class Meta:
        ordering = ['-id'] 


class Nota(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100, blank= True, null=True)
    contenido = models.TextField(max_length=1000)
    etiqueta = models.ManyToManyField(Etiqueta, blank=True, default='')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, default='')

    bg_primary = 'bg-primary' 
    bg_secondary = 'bg-secondary'
    bg_success = 'bg-success'
    bg_danger = 'bg-danger'
    bg_warning = 'bg-warning'
    bg_info = 'bg-info'
    bg_light = 'bg-light'
    bg_dark = 'bg-dark'

    COLORES_CHOICES = {
        bg_primary : 'bg-primary', 
        bg_secondary : 'bg-secondary',
        bg_success : 'bg-success',
        bg_danger : 'bg-danger',
        bg_warning : 'bg-warning',
        bg_info : 'bg-info',
        bg_light : 'bg-light',
        bg_dark : 'bg-dark',
    }
    color_fondo = models.CharField(
        max_length=20,
        choices=COLORES_CHOICES,
        default=bg_danger,
    )
    def __str__(self):
        return self.titulo
    
    def save(self, *args, **kwargs):
        if not self.titulo:
            self.titulo = self.contenido.split()[0]
            if len(self.titulo) <= 4:
                self.titulo = self.contenido.split()[0:2]
                self.titulo = " ".join(self.titulo)
            
        self.slug = slugify(self.titulo)
        super(Nota, self).save()  

    def get_update_url(self):
        return reverse('notas:modificar_nota', args=[self.pk])
    
    def get_detele_url(self):
        return reverse('notas:borrar_nota', args=[self.pk])

  
    class Meta:
        ordering =['-id']   



