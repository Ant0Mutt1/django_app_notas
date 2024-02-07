from django.forms import Form
from django.forms import CharField
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_forms.layout import Field
from crispy_forms.layout import Submit

from .models import Nota
from .models import Etiqueta



class NotaForm(ModelForm):
    class Meta:
        model = Nota
        fields = ["titulo", "contenido", "color_fondo", "etiqueta" ]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Obtener el usuario actual del argumento 'user'
        super().__init__(*args, **kwargs)

        # Filtrar las etiquetas del usuario actual
        etiquetas_del_usuario = Etiqueta.objects.filter(usuario=user)

        self.fields['etiqueta'].queryset = etiquetas_del_usuario  # Asignar el conjunto de consultas filtrado

        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Field('titulo'),
            Field('contenido'),
            Field('etiqueta', template="notas/custom_checkbox_button.html"),
            Submit('guardar', 'Guardar', css_class="mt-3"),  
            Field('color_fondo', template="notas/color_circle.html"),
        )
class EtiquetaForm(ModelForm):
    class Meta:
        model = Etiqueta
        fields = ["nombre"]     
    def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.helper = FormHelper(self)   
      self.helper.add_input(Submit('guardar','Guardar', css_class="mt-3"))

class BusquedaForm(Form):
   query = CharField(label='', max_length=100)
