from rest_framework import serializers
from .models import *


class ComunaSerializer(serializers.ModelSerializer):
    # tipo = serializer(readonly=true),
    class Meta:
        model = Comuna
        fields = '__all__'
class TipoUsuarioSerializer(serializers.ModelSerializer):
    # tipo = serializer(readonly=true),
    class Meta:
        model = TipoUsuario
        fields = '__all__'
class RegionSerializer(serializers.ModelSerializer):
    # tipo = serializer(readonly=true),
    class Meta:
        model = Region
        fields = '__all__'
class CuentaSerializer(serializers.ModelSerializer):
    # tipo = serializer(readonly=true),
    class Meta:
        model = Cuenta
        fields = '__all__'
class UsuarioSerializer(serializers.ModelSerializer):
    # tipo = serializer(readonly=true),
    class Meta:
        model = Usuario
        fields = '__all__'
class TipoObraSerializer(serializers.ModelSerializer):
    # tipo = serializer(readonly=true),
    class Meta:
        model = TipoObra
        fields = '__all__'
class SolicitudObraSerializer(serializers.ModelSerializer):
    # tipo = serializer(readonly=true),
    class Meta:
        model = SolicitudObra
        fields = '__all__'
class ObraSerializer(serializers.ModelSerializer):
    # tipo = serializer(readonly=true),
    class Meta:
        model = Obra
        fields = '__all__'
class EstadoCompraSerializer(serializers.ModelSerializer):
    # tipo = serializer(readonly=true),
    class Meta:
        model = EstadoCompra
        fields = '__all__'
class CompraSerializer(serializers.ModelSerializer):
    # tipo = serializer(readonly=true),
    class Meta:
        model = Compra
        fields = '__all__'
class AutentificacionSerializer(serializers.ModelSerializer):
    # tipo = serializer(readonly=true),
    class Meta:
        model = Autentificacion
        fields = '__all__'
class TipoBancoSerializer(serializers.ModelSerializer):
    # tipo = serializer(readonly=true),
    class Meta:
        model = TipoBanco
        fields = '__all__'
class TipoCuentaSerializer(serializers.ModelSerializer):
    # tipo = serializer(readonly=true),
    class Meta:
        model = TipoCuenta
        fields = '__all__'
class DatosCooperativosSerializer(serializers.ModelSerializer):
    # tipo = serializer(readonly=true),
    class Meta:
        model = DatosCooperativos
        fields = '__all__'
