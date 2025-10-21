from django import forms
from django.contrib.auth.models import User
from .models import Servicios, Establecimientos, Proveedor, TipoRecibo, RegistroServicio

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicios
        fields = ['numero_servicio', 'establecimiento', 'proveedor', 'tipo_recibo']
        labels = {
            'numero_servicio': 'Número de Servicio',
            'establecimiento': 'Establecimiento',
            'proveedor': 'Proveedor',
            'tipo_recibo': 'Tipo de Recibo'
        }
        widgets = {
            'numero_servicio': forms.TextInput(attrs={'class': 'form-control'}),
            'establecimiento': forms.Select(attrs={'class': 'form-select'}),
            'proveedor': forms.Select(attrs={'class': 'form-select'}),
            'tipo_recibo': forms.Select(attrs={'class': 'form-select'})
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['establecimiento'].queryset = Establecimientos.objects.all()
            self.fields['proveedor'].queryset = Proveedor.objects.all()
            self.fields['tipo_recibo'].queryset = TipoRecibo.objects.all()

class EstablecimientoForm(forms.ModelForm):
    class Meta:
        model = Establecimientos
        fields = ['nombre', 'rbd', 'direccion', 'email', 'director']
        labels = {
            'nombre': 'Nombre del Establecimiento',
            'rbd': 'RBD',
            'direccion': 'Dirección',
            'email': 'Correo Electrónico',
            'director': 'Director'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'rbd': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'director': forms.Select(attrs={'class': 'form-select'})
        }

    
class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'rut', 'tipo_proveedor']
        labels = {
            'nombre': 'Nombre del Proveedor',
            'rut': 'RUT',   
            'tipo_proveedor': 'Tipo de Proveedor'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'rut': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_proveedor': forms.Select(attrs={'class': 'form-select'})
        }

class TipoReciboForm(forms.ModelForm):
    class Meta:
        model = TipoRecibo
        fields = ['nombre']
        labels = {
            'nombre': 'Nombre del Tipo de Recibo'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'})
        }

class RegistroServicioForm(forms.ModelForm):
    class Meta:
        model = RegistroServicio
        fields = [
            'servicio',
            'numero_recibo',
            'fecha_envio_pago',
            'fecha_emision',
            'fecha_vencimiento',
            'monto',
            'interes'
        ]
        widgets = {
            'servicio': forms.Select(attrs={'class': 'form-select'}),
            'numero_recibo': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_envio_pago': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
            'fecha_emision': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
            'fecha_vencimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
            'monto': forms.NumberInput(attrs={'class': 'form-control', 'step': '1', 'min': '0'}),
            'interes': forms.NumberInput(attrs={'class': 'form-control', 'step': '1', 'min': '0'})
        }

    def __init__(self, *args, **kwargs):
        self.establecimiento_id = kwargs.pop('establecimiento_id', None)
        super().__init__(*args, **kwargs)
        
        # Configurar el formato de entrada para los campos de fecha
        self.fields['fecha_envio_pago'].input_formats = ['%Y-%m-%d']
        self.fields['fecha_emision'].input_formats = ['%Y-%m-%d']
        self.fields['fecha_vencimiento'].input_formats = ['%Y-%m-%d']
        
        # Filtrar servicios por establecimiento si se proporciona
        if self.establecimiento_id:
            self.fields['servicio'].queryset = Servicios.objects.filter(establecimiento_id=self.establecimiento_id)
        else:
            self.fields['servicio'].queryset = Servicios.objects.all()

class PerfilUsuarioForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo Electrónico'
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'})
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Hacer el campo email requerido
        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True


class ProcesarPlanillaForm(forms.Form):
    TIPO_CHOICES = [
        ('bancos', 'Con Cuenta'),
        ('vale_vista', 'Sin Cuenta (Vale Vista)')
    ]
    
    tipo_proceso = forms.ChoiceField(
        choices=TIPO_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
        label='Tipo de Proceso',
        initial='bancos'
    )
    
    archivo = forms.FileField(
        widget=forms.FileInput(attrs={'class': 'form-control', 'accept': '.xlsx,.xls'}),
        label='Archivo Excel',
        help_text='Seleccione un archivo Excel (.xlsx o .xls)'
    )
    
