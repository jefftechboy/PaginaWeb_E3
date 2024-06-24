from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from datetime import datetime
from captcha.fields import CaptchaField
from django_recaptcha.fields import ReCaptchaField


class TipoUsuarioForm(ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = TipoUsuario
        fields = '__all__'

class ComunaForm(ModelForm):
    #captcha = CaptchaField()
    captcha = ReCaptchaField()
    class Meta:
        model = Comuna
        fields = '__all__'

class RegionForm(ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = Region
        fields = '__all__'

class CuentaForm(ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = Cuenta
        fields = '__all__'

class UsuarioForm(ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = Usuario
        fields = '__all__'

class TipoObraForm(ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = TipoObra
        fields = '__all__'


class SolicitudObraForm(ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = SolicitudObra
        fields = '__all__'







class ObraForm(forms.ModelForm):
    class Meta:
        model = Obra
        fields = '__all__'
        exclude = ['fechaIngreso','NombreUsuario']
        fechaIngreso = initial = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        widgets = {
            'codigo': forms.TextInput(attrs={'readonly': 'readonly'}),
        }

           





                
                    
class CompraForm(ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Obtiene el usuario actual pasado como argumento
        super(CompraForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['Usuario'].initial = user.username  # Establece el nombre de usuario como valor inicial para el campo Usuario

    class Meta:
        exclude = ['fechaCompra']
        fechaCompra = initial = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        model = Compra
        fields = '__all__'




class TipoBancoForm(ModelForm):
    class Meta:
        model = TipoBanco
        fields = '__all__'

class TipoCuentaForm(ModelForm):
    class Meta:
        model = TipoCuenta
        fields = '__all__'

class DatosCooperativosForm(forms.ModelForm):
    class Meta:
        model = DatosCooperativos
        fields = '__all__'  # Esto incluirá todos los campos del modelo
        widgets = {
            'NombreCuentaCooperativo': forms.TextInput(attrs={'class': 'form-control'}),
            'NombreCliente': forms.TextInput(attrs={'class': 'form-control'}),
            'Correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'Direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'Telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'Banco': forms.Select(attrs={'class': 'form-control'}),  # Si Banco es un ForeignKey
            'TipoCuenta': forms.Select(attrs={'class': 'form-control'}),  # Si TipoCuenta es un ForeignKey
            'NroCuenta': forms.TextInput(attrs={'class': 'form-control'}),
            'imagenCooperativo': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }

class AutentificacionForm(forms.ModelForm):
    class Meta:
        model = Autentificacion
        fields = ['NombreCliente', 'Correo', 'Direccion', 'Telefono', 'imagenAutentificacion']
        widgets = {
            'NombreCliente': forms.TextInput(attrs={'class': 'form-control'}),
            'Correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'Direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'Telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'imagenAutentificacion': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']

