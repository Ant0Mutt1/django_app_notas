from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic import View

from .forms import BusquedaForm
from .forms import NotaForm
from .forms import EtiquetaForm
from .models import Nota
from .models import Etiqueta
from usuarios.mixins import CustomLoginRequiredMixin



class IndexView(CustomLoginRequiredMixin, View):
    template_name = 'notas/index.html'
    items_per_page = 6  

    def get(self, request, slug=None):
        context = {}
        form_etiqueta = EtiquetaForm()
        context['form_etiqueta'] = form_etiqueta
        form_nota = NotaForm(user=request.user)
        context['form_nota'] = form_nota

        if slug is None:
            notas = Nota.objects.filter(usuario = self.request.user)
        else:
            notas = Nota.objects.filter(usuario = self.request.user, etiqueta__slug=slug)

        # Paginación
        paginator = Paginator(notas, self.items_per_page)
        page = request.GET.get('page')

        try:
            notas_paginadas = paginator.page(page)
        except PageNotAnInteger:
            notas_paginadas = paginator.page(1)
        except EmptyPage:
            notas_paginadas = paginator.page(paginator.num_pages)

        context['notas'] = notas_paginadas

        etiquetas = Etiqueta.objects.annotate(num_notas=Count('nota')).filter(usuario = self.request.user).order_by('-num_notas')
        context['etiquetas'] = etiquetas

        return render(request, self.template_name, context)

class EtiquetaCreate(CustomLoginRequiredMixin, CreateView):
    model = Etiqueta
    template_name = 'notas/crear_etiqueta.html'
    form_class = EtiquetaForm

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER', reverse_lazy('notas:index'))

class NotaCreate(CustomLoginRequiredMixin, CreateView):
    model = Nota
    template_name = 'notas/crear_nota.html'
    form_class = NotaForm

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(NotaCreate, self).get_form_kwargs()
        kwargs['user'] = self.request.user  # Pasar el usuario actual al formulario
        return kwargs

    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER', reverse_lazy('notas:index'))


class NotaList(CustomLoginRequiredMixin, ListView):
    model = Nota
    template_name ='notas/lista_nota.html'

    def get_queryset(self):
        return Nota.objects.filter(usuario = self.request.user)

class EtiquetaList(CustomLoginRequiredMixin, ListView):
    model = Etiqueta
    template_name ='notas/etiqueta_nota.html'
    
    def get_queryset(self):
        return Etiqueta.objects.filter(usuario = self.request.user)
  
class NotaDelete(CustomLoginRequiredMixin, DeleteView):
    model = Nota
    template_name = 'notas/borrar_nota.html' 

    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER', reverse_lazy('notas:index'))

class EtiquetaDelete(CustomLoginRequiredMixin, DeleteView):
    model = Etiqueta
    template_name = 'notas/borrar_etiqueta.html' 

    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER', reverse_lazy('notas:index')) 

class NotaDetalle(CustomLoginRequiredMixin, DetailView):
    model = Nota
    template_name ='notas/detalle_nota.html'

class NotaUpdate(CustomLoginRequiredMixin, UpdateView):
    model = Nota
    form_class = NotaForm
    template_name = 'notas/modificar_nota.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  
        return kwargs
    
    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER', reverse_lazy('notas:index'))

class EtiquetaUpdate(CustomLoginRequiredMixin, UpdateView):
    model = Etiqueta
    form_class = EtiquetaForm
    template_name = 'notas/modificar_etiqueta.html'

    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER', reverse_lazy('notas:index'))

class NotaBuscar(CustomLoginRequiredMixin, View):
    template_name = 'notas/buscar_nota.html'
    results = ''

    def get(self, request):
        form = BusquedaForm()
        return render(request, self.template_name, {'form': form, 'results':self.results })
    
    def post(self, request):
        form = BusquedaForm(request.POST)
        form_etiqueta = EtiquetaForm()
        form_nota = NotaForm(user=request.user)
        etiquetas = Etiqueta.objects.annotate(num_notas=Count('nota')).filter(usuario = self.request.user).order_by('-num_notas')

        if form.is_valid():
            query = form.cleaned_data['query']
            results = Nota.objects.filter(usuario = self.request.user, titulo__icontains=query)

        
        return render(request, self.template_name, {'form': form, 'results': results, 'form_etiqueta':form_etiqueta,'form_nota':form_nota, 'etiquetas':etiquetas })



