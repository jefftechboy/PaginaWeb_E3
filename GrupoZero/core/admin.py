from django.contrib import admin
from .models import *
from django.contrib.admin import ModelAdmin
from admin_confirm import AdminConfirmMixin

class ComunaAdmin(AdminConfirmMixin,ModelAdmin):
    confirm_change = True
    confirmation_fields=['descripcion']

# Register your models here.
admin.site.register(Comuna,ComunaAdmin)

admin.site.register(TipoUsuario)
admin.site.register(Region)
admin.site.register(Cuenta)
admin.site.register(Usuario)
admin.site.register(TipoObra)
admin.site.register(SolicitudObra)
admin.site.register(Obra)
admin.site.register(Compra)
admin.site.register(Autentificacion)
admin.site.register(TipoBanco)
admin.site.register(TipoCuenta)
admin.site.register(EstadoCompra)
admin.site.register(DatosCooperativos)