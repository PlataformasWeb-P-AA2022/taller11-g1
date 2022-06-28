from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms

from administrativo.models import Edificio, Departamento

class EdificioForm(ModelForm):
    class Meta:
        model = Edificio
        fields = ['nombre', 'direccion', 'ciudad', 'tipo']
        labels = {
            'nombre': _('Ingrese nombre por favor'),
            'direccion': _('Ingrese la direccion'),
            'ciudad': _('Ingrese la ciudad por favor'),
            'tipo': _('Ingrese el tipo por favor'),
        }


    def clean_nombre(self):
        valor = self.cleaned_data['nombre']
        num_palabras = len(valor.split())

        if num_palabras < 2:
            raise forms.ValidationError("Ingrese dos nombre por favor")
        return valor

    def clean_direccion(self):
        valor = self.cleaned_data['direccion']
        return valor

    def clean_ciudad(self):
        valor = self.cleaned_data['ciudad']
        num_palabras = len(valor.split())

        if num_palabras < 1:
            raise forms.ValidationError("Ingrese una ciudad ")
        return valor

    def clean_tipo(self):
        valor = self.cleaned_data['tipo']
        num_palabras = len(valor.split())

        if num_palabras < 1:
            raise forms.ValidationError("Seleccione uno por favor")
        return valor


class NumeroDepaForm(ModelForm):
    class Meta:
        model = Departamento
        fields = ['nombre', 'costo_depa', 'num_cuartos',  'edificio']


class NumeroDepaEdificioForm(ModelForm):

    def __init__(self, edificio, *args, **kwargs):
        super(NumeroDepaEdificioForm, self).__init__(*args, **kwargs)
        self.initial['edificio'] = edificio
        self.fields["edificio"].widget = forms.widgets.HiddenInput()
        print(edificio)

    class Meta:
        model = Departamento
        fields = ['nombre', 'costo_depa', 'num_cuartos',  'edificio']
