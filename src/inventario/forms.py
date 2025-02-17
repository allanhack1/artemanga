from venta.models import Despacho, Venta
from .models import Producto, Genero
from catalogo.models import Oferta
from django import forms


class ProductoBodegaForm(forms.ModelForm):
    fecha_publicacion = forms.DateField(
        widget=forms.DateInput(attrs={
            'id': 'datepicker',
            'data-date-format': 'dd/mm/yyyy',
            'data-date-language': 'es',
        }),
    )

    genero = forms.ModelMultipleChoiceField(
        queryset=Genero.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Producto
        exclude = ['es_destacado', 'esta_publicado']


class ActualizarProductoVentasForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['es_nuevo', 'es_destacado', 'esta_publicado', 'precio']


class ActualizarVentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['estado', 'imagen_deposito', 'boleta']

        imagen_deposito = forms.ImageField(required=False, widget=forms.FileInput)
        boleta = forms.FileField(required=False, widget=forms.ClearableFileInput(attrs={'multiple': False}))


class DespachoForm(forms.ModelForm):
    class Meta:
        model = Despacho
        fields = ['estado', 'codigo_seguimiento']
        labels = {
            'estado': 'Estado del despacho'
        }


class OfertaForm(forms.ModelForm):
    fecha_inicio = forms.DateField(
        widget=forms.DateInput(attrs={
            'id': 'oferta_fecha_inicio',
            'data-date-format': 'dd/mm/yyyy',
            'data-date-language': 'es',
        }),
    )

    fecha_fin = forms.DateField(
        widget=forms.DateInput(attrs={
            'id': 'oferta_fecha_fin',
            'data-date-format': 'dd/mm/yyyy',
            'data-date-language': 'es',
        }),
    )

    class Meta:
        model = Oferta
        fields = ['producto', 'descuento', 'fecha_inicio', 'fecha_fin']
