from django.urls import path
from .views import IndexView
from .views import EtiquetaCreate
from .views import NotaCreate
from .views import NotaList
from .views import EtiquetaList
from .views import NotaDelete
from .views import EtiquetaDelete
from .views import NotaDetalle
from .views import NotaUpdate
from .views import EtiquetaUpdate
from .views import NotaBuscar

app_name='notas'
urlpatterns = [
  path('', IndexView.as_view(), name='index'),
  path('home/', IndexView.as_view(), name='index'),
  path('notas/<slug:slug>/', IndexView.as_view(), name='index_con_slug'),
  path('notas/post/', IndexView.as_view(), name='index_post'),
  path('crear_etiqueta', EtiquetaCreate.as_view(), name='crear_etiqueta'),
  path('crear_nota', NotaCreate.as_view(), name='crear_nota'),
  path('lista_nota', NotaList.as_view(), name='lista_nota'),
  path('lista_etiqueta', EtiquetaList.as_view(), name='lista_etiqueta'),
  path('borrar_nota/<int:pk>', NotaDelete.as_view(), name='borrar_nota'), 
  path('borrar_etiqueta/<int:pk>', EtiquetaDelete.as_view(), name='borrar_etiqueta'), 
  path('detalle_nota/<int:pk>', NotaDetalle.as_view(), name='detalle_nota'), 
  path('modificar_nota/<int:pk>', NotaUpdate.as_view(), name='modificar_nota'), 
  path('modificar_etiqueta/<int:pk>', EtiquetaUpdate.as_view(), name='modificar_etiqueta'), 
  path('busqueda/', NotaBuscar.as_view(), name='buscar'), 
]
