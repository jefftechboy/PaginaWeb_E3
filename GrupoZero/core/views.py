
# Create your views here.
from django.shortcuts import render, redirect
from .views import *
from .models import *
from .forms import *
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import Group,User
from django.contrib import messages
from rest_framework import viewsets
from .serializers import *
from rest_framework.renderers import JSONRenderer
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth.decorators import user_passes_test,login_required

import requests


def GrupoCooperativos(group_name,group_name2):
    def in_group(u):
        if u.is_authenticated:
            if u.groups.filter(name=group_name).exists() or u.is_superuser:
                return True
            elif u.groups.filter(name=group_name2).exists() or u.is_superuser:
                return True
        return False
    return user_passes_test(in_group)

def Comunaapi(request):
    response = requests.get('http://127.0.0.1:8000/api/Comuna/')
    comunas = response.json()
    aux = {
        'lista' : comunas
    }
    return render(request,'core/administracion/crudapi/comunaapi.html',aux)



class ComunaViewSet(viewsets.ModelViewSet):
    queryset = Comuna.objects.all().order_by('id')
    serializer_class =  ComunaSerializer
    renderer_classes = [JSONRenderer]
    
class TipoUsuarioViewSet(viewsets.ModelViewSet):
    queryset = TipoUsuario.objects.all().order_by('id')
    serializer_class =  TipoUsuarioSerializer
    renderer_classes = [JSONRenderer]
    
class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all().order_by('id')
    serializer_class =  RegionSerializer
    renderer_classes = [JSONRenderer]
    
class CuentaViewSet(viewsets.ModelViewSet):
    queryset = Cuenta.objects.all().order_by('id')
    serializer_class =  CuentaSerializer
    renderer_classes = [JSONRenderer]
    

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all().order_by('id')
    serializer_class =  UsuarioSerializer
    renderer_classes = [JSONRenderer]
    


class TipoObraViewSet(viewsets.ModelViewSet):
    queryset = TipoObra.objects.all().order_by('id')
    serializer_class =  TipoObraSerializer
    renderer_classes = [JSONRenderer]
    

class SolicitudObraViewSet(viewsets.ModelViewSet):
    queryset = SolicitudObra.objects.all().order_by('id')
    serializer_class =  SolicitudObraSerializer
    renderer_classes = [JSONRenderer]
    

class ObraViewSet(viewsets.ModelViewSet):
    queryset = Obra.objects.all().order_by('id')
    serializer_class =  ObraSerializer
    renderer_classes = [JSONRenderer]
    


class EstadoCompraViewSet(viewsets.ModelViewSet):
    queryset = EstadoCompra.objects.all().order_by('id')
    serializer_class =  EstadoCompraSerializer
    renderer_classes = [JSONRenderer]
    


class CompraViewSet(viewsets.ModelViewSet):
    queryset = Compra.objects.all().order_by('id')
    serializer_class =  CompraSerializer
    renderer_classes = [JSONRenderer]
    

class AutentificacionViewSet(viewsets.ModelViewSet):
    queryset = Autentificacion.objects.all().order_by('id')
    serializer_class =  AutentificacionSerializer
    renderer_classes = [JSONRenderer]
    

class TipoBancoViewSet(viewsets.ModelViewSet):
    queryset = TipoBanco.objects.all().order_by('id')
    serializer_class =  TipoBancoSerializer
    renderer_classes = [JSONRenderer]
    

class TipoCuentaViewSet(viewsets.ModelViewSet):
    queryset = TipoCuenta.objects.all().order_by('id')
    serializer_class =  TipoCuentaSerializer
    renderer_classes = [JSONRenderer]
    



class DatosCooperativosViewSet(viewsets.ModelViewSet):
    queryset = DatosCooperativos.objects.all().order_by('id')
    serializer_class =  DatosCooperativosSerializer
    renderer_classes = [JSONRenderer]
    







def account_locked(request):
    return render(request,'core/account_locked.html')

def inicio(request):
    cuentas = Autentificacion.objects.all()
    aux = {
        'cuentasAutentificadas' : cuentas
    }
    return render(request,'core/inicio.html',aux)
def cuentaCliente(request):
    return render(request,'core/cliente.html')
def tienda(request):

    obras = Obra.objects.all()

    page = request.GET.get('page',1)

    try:
        paginator = Paginator(obras,8)
        obras = paginator.page(page)
    except:
        raise Http404
    aux = {
        'entity' : obras,
        'paginator': paginator,
        'form': CompraForm(user=request.user)
    }
    if request.method == 'POST':
        formulario = CompraForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"COMPRA AGREGADA AL CARRITO")
            return render(request,'core/tienda.html',aux)
        else:
            aux['form'] = formulario
    return render(request,'core/tienda.html',aux)







def pago(request):
    return render(request,'core/pago.html')
def contacto(request):
    return render(request,'core/contacto.html')
def equipo(request):
    return render(request,'core/equipo.html')


def carroCompra(request):
    obrasDatos = Obra.objects.all()
    comprasDatos = Compra.objects.filter(Usuario= request.user.username)
    aux = {
        'obras' : obrasDatos,
        'compras': comprasDatos
    }
    return render(request,'core/carroCompra.html',aux)


def error404(request):
    return render(request,'core/404.html')
def informacionCompra(request):
    return render(request,'core/informacionCompra.html')
def login(request):
    return render(request,'core/login.html')
@login_required
@GrupoCooperativos('EjecutivoAdministrador','admin')
def administracion(request):
    return render(request,'core/administracion/administracion.html')


#CRUD CUENTA COOPRATIVO
@login_required
def CuentaCooperativos(request):
    cooperativos = DatosCooperativos.objects.all()
    obras = Obra.objects.filter(NombreUsuario= request.user.username)
    aux = {
        'lista' : cooperativos,
        'listaObras' : obras
    }
    return render(request,'core/cooperativo.html',aux)




    aux = {
        'entity' : usuarios,
        'paginator': paginator
    }



# CRUD Cooperativos
@login_required
@GrupoCooperativos('EjecutivoAdministrador','admin')
def DatosCuentaCooperativo(request):
    cooperativos = DatosCooperativos.objects.all()
    page = request.GET.get('page',1)
    try:
        paginator = Paginator(cooperativos,1)
        cooperativos = paginator.page(page)
    except:
        raise Http404
    aux = {
        'entity' : cooperativos,
        'paginator': paginator
    }
    return render(request,'core/administracion/DatosCooperativos/listaDatosCooperativos.html',aux)
# AGREGAR 
@login_required
def agregarDatosCooperativos(request):
    aux = {
        'form': DatosCooperativosForm()
    }
    if request.method == 'POST':
        formulario = DatosCooperativosForm(data=request.POST,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request," COOPERATIVO AGREGADO CORRECTAMENTE")
            return redirect(to="DatosCuentaCooperativo")
        else:
            aux['form'] = formulario

    return render(request,'core/administracion/DatosCooperativos/agregarDatosCooperativos.html',aux)
#ACTUALIZAR
@login_required
@GrupoCooperativos('EjecutivoAdministrador','admin')
def actualizarDatosCooperativos(request,id):
    usuario = DatosCooperativos.objects.get(id=id)
    aux = {
        'form': DatosCooperativosForm(instance=usuario)
    }
    if request.method == 'POST':
        formulario = DatosCooperativosForm(request.POST,instance=usuario,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            aux['form'] = formulario
            messages.success(request,"DATO DE COOPERATIVO ACTUALIZADO CORRECTAMENTE")
            return redirect(to="DatosCuentaCooperativo")
        else:
            aux['form'] = formulario   

    return render(request,'core/administracion/DatosCooperativos/actualizarDatosCooperativos.html',aux)
#ELIMINAR
@login_required
@GrupoCooperativos('EjecutivoAdministrador','admin')
def eliminarDatosCooperativos(request,id):
    usuario = DatosCooperativos.objects.get(id=id)
    usuario.delete()
    messages.success(request,"DATOS DE COOPERATIVO ELIMINADO CORRECTAMENTE")
    return redirect(to="DatosCuentaCooperativo")


# CRUD USUARIO

# LISTAR 
@login_required
@GrupoCooperativos('EjecutivoAdministrador','admin')
def listado(request):
    usuarios = Usuario.objects.all()
    page = request.GET.get('page',1)
    try:
        paginator = Paginator(usuarios,1)
        usuarios = paginator.page(page)
    except:
        raise Http404

    aux = {
        'entity' : usuarios,
        'paginator': paginator
    }
    return render(request,'core/listado.html',aux)
# AGREGAR 
@login_required
@GrupoCooperativos('EjecutivoAdministrador','admin')
def ad(request):
    aux = {
        'form': UsuarioForm()
    }
    if request.method == 'POST':
        formulario = UsuarioForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"USUARIO AGREGADO CORRECTAMENTE")
            return redirect(to="listado")
        else:
            aux['form'] = formulario

    return render(request,'core/ad.html',aux)
# ACTUALIZAR 
@login_required
@GrupoCooperativos('EjecutivoAdministrador','admin')
def update(request,id):
    usuario = Usuario.objects.get(id=id)
    aux = {
        'form': UsuarioForm(instance=usuario)
    }
    if request.method == 'POST':
        formulario = UsuarioForm(request.POST,instance=usuario)
        if formulario.is_valid():
            formulario.save()
            aux['form'] = formulario
            messages.success(request,"USUARIO MODIFICADO CORRECTAMENTE")
            return redirect(to="listado")
        else:
            aux['form'] = formulario   

    return render(request,'core/update.html',aux)
# ELIMINAR 
@login_required
@GrupoCooperativos('EjecutivoAdministrador','admin')
def delete(request,id):
    usuario = Usuario.objects.get(id=id)
    usuario.delete()
    messages.success(request,"USUARIO AGREGADO CORRECTAMENTE")
    return redirect(to="listado")


#CRUD REGION

#LISTAR
@login_required
@GrupoCooperativos('EjecutivoAdministrador','admin')
def listadoRegion(request):
    regiones = Region.objects.all()

    page = request.GET.get('page',1)

    try:
        paginator = Paginator(regiones,6)
        regiones = paginator.page(page)
    except:
        raise Http404
        
    aux = {
        'entity' : regiones,
        'paginator': paginator
    }

    return render(request,'core/administracion/regiones/regionLista.html',aux)
# AGREGAR 
@login_required
@GrupoCooperativos('EjecutivoAdministrador','admin')
def agregarRegion(request):
    aux = {
        'form': RegionForm()
    }
    if request.method == 'POST':
        formulario = RegionForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"REGION AGREGADA CORRECTAMENTE")
            return redirect(to="listadoRegion")
        else:
            aux['form'] = formulario

    return render(request,'core/administracion/regiones/regionAgregar.html',aux)
# ACTUALIZAR 
@login_required
@GrupoCooperativos('EjecutivoAdministrador','admin')
def actualizarRegion(request,id):
    usuario = Region.objects.get(id=id)
    aux = {
        'form': RegionForm(instance=usuario)
    }
    if request.method == 'POST':
        formulario = RegionForm(request.POST,instance=usuario)
        if formulario.is_valid():
            formulario.save()
            aux['form'] = formulario
            messages.success(request,"REGION MODIFICADA CORRECTAMENTE")
            return redirect(to="listadoRegion")
        else:
            aux['form'] = formulario   

    return render(request,'core/administracion/regiones/regionActualizar.html',aux)
# ELIMINAR 
@login_required
@GrupoCooperativos('EjecutivoAdministrador','admin')
def eliminarRegion(request,id):
    usuario = Region.objects.get(id=id)
    usuario.delete()
    messages.success(request,"REGION ELIMINADA CORRECTAMENTE")
    return redirect(to="listadoRegion")


#CRUD Tipo Banco

#LISTAR
@login_required
@GrupoCooperativos('EjecutivoAdministrador','admin')
def listadoTipoBanco(request):
    tipoBancos = TipoBanco.objects.all()

    page = request.GET.get('page',1)

    try:
        paginator = Paginator(tipoBancos,6)
        tipoBancos = paginator.page(page)
    except:
        raise Http404
        
    aux = {
        'entity' : tipoBancos,
        'paginator': paginator
    }
    return render(request,'core/administracion/TipoBanco/listadoTipoBanco.html',aux)
# AGREGAR 
@login_required
@GrupoCooperativos('EjecutivoAdministrador','admin')
def agregarTipoBanco(request):
    aux = {
        'form': TipoBancoForm()
    }
    if request.method == 'POST':
        formulario = TipoBancoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"TIPO BANCO AGREGADO CORRECTAMENTE")
            return redirect(to="listadoTipoBanco")
        else:
            aux['form'] = formulario

    return render(request,'core/administracion/TipoBanco/agregarTipoBanco.html',aux)
# ACTUALIZAR 
@login_required
@GrupoCooperativos('EjecutivoAdministrador','admin')
def actualizarTipoBanco(request,id):
    usuario = TipoBanco.objects.get(id=id)
    aux = {
        'form': TipoBancoForm(instance=usuario)
    }
    if request.method == 'POST':
        formulario = TipoBancoForm(request.POST,instance=usuario)
        if formulario.is_valid():
            formulario.save()
            aux['form'] = formulario
            messages.success(request,"TIPO DE BANCO MODIFICADO CORRECTAMENTE")
            return redirect(to="listadoTipoBanco")
        else:
            aux['form'] = formulario   

    return render(request,'core/administracion/TipoBanco/actualizarTipoBanco.html',aux)
# ELIMINAR 
@login_required
@GrupoCooperativos('EjecutivoAdministrador','admin')
def eliminarTipoBanco(request,id):
    usuario = TipoBanco.objects.get(id=id)
    usuario.delete()
    messages.success(request,"TIPO DE BANCO ELIMINADO CORRECTAMENTE")
    return redirect(to="listadoTipoBanco")


#CRUD Tipo Cuentas

#LISTAR
@login_required
@GrupoCooperativos('EjecutivoAdministrador','admin')
def listadoTipoCuentas(request):
    tipoCuenta = TipoCuenta.objects.all()
    page = request.GET.get('page',1)

    try:
        paginator = Paginator(tipoCuenta,6)
        tipoCuenta = paginator.page(page)
    except:
        raise Http404
        
    aux = {
        'entity' : tipoCuenta,
        'paginator': paginator
    }
    return render(request,'core/administracion/TipoCuentaBancaria/listaTipoCuentaBancaria.html',aux)
# AGREGAR 
@login_required
@GrupoCooperativos('EjecutivoAdministrador','admin')
def agregarTipoCuentas(request):
    aux = {
        'form': TipoCuentaForm()
    }
    if request.method == 'POST':
        formulario = TipoCuentaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"TIPO DE CUENTA AGREGADA CORRECTAMENTE")
            return redirect(to="listadoTipoCuentas")
        else:
            aux['form'] = formulario

    return render(request,'core/administracion/TipoCuentaBancaria/agregarTipoCuentaBancaria.html',aux)
# ACTUALIZAR 
@login_required
@GrupoCooperativos('EjecutivoAdministrador','admin')
def actualizarTipoCuentas(request,id):
    usuario = TipoCuenta.objects.get(id=id)
    aux = {
        'form': TipoCuentaForm(instance=usuario)
    }
    if request.method == 'POST':
        formulario = TipoCuentaForm(request.POST,instance=usuario)
        if formulario.is_valid():
            formulario.save()
            aux['form'] = formulario
            messages.success(request,"TIPO DE CUENTA MODIFICADA CORRECTAMENTE")
            return redirect(to="listadoTipoCuentas")
        else:
            aux['form'] = formulario   

    return render(request,'core/administracion/TipoCuentaBancaria/actualizarTipoCuentaBancaria.html',aux)
# ELIMINAR 
@login_required
@GrupoCooperativos('EjecutivoAdministrador','admin')
def eliminarTipoCuentas(request,id):
    usuario = TipoCuenta.objects.get(id=id)
    usuario.delete()
    messages.success(request,"TIPO DE CUENTA ELIMINADA CORRECTAMENTE")
    return redirect(to="listadoTipoCuentas")



#CRUD COMUNA

#LISTADO
@login_required
@GrupoCooperativos('EjecutivoAdministrador','admin')
def listadoComuna(request):
    comunas = Comuna.objects.all()
    page = request.GET.get('page',1)

    try:
        paginator = Paginator(comunas,6)
        comunas = paginator.page(page)
    except:
        raise Http404
        
    aux = {
        'entity' : comunas,
        'paginator': paginator
    }
    return render(request,'core/administracion/comunas/comunaLista.html',aux)
# AGREGAR 
@login_required
@GrupoCooperativos('EjecutivoAdministrador','admin')
def agregarComuna(request):
    aux = {
        'form': ComunaForm()
    }
    if request.method == 'POST':
        formulario = ComunaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"COMUNA AGREGADA CORRECTAMENTE")
            return redirect(to="listadoComuna")
        else:
            aux['form'] = formulario

    return render(request,'core/administracion/comunas/comunaAgregar.html',aux)
# ACTUALIZAR 
@login_required
@GrupoCooperativos('EjecutivoAdministrador','admin')
def actualizarComuna(request,id):
    usuario = Comuna.objects.get(id=id)
    aux = {
        'form': ComunaForm(instance=usuario)
    }
    if request.method == 'POST':
        formulario = ComunaForm(request.POST,instance=usuario)
        if formulario.is_valid():
            formulario.save()
            aux['form'] = formulario
            messages.success(request,"COMUNA ACTUALIZADA CORRECTAMENTE")
            return redirect(to="listadoComuna")
        else:
            aux['form'] = formulario   

    return render(request,'core/administracion/comunas/comunaActualizar.html',aux)
# ELIMINAR 
@login_required
@GrupoCooperativos('EjecutivoAdministrador','admin')
def eliminarComuna(request,id):
    usuario = Comuna.objects.get(id=id)
    usuario.delete()
    messages.success(request,"COMUNA ELIMINADA CORRECTAMENTE")
    return redirect(to="listadoComuna")




#CRUD TIPO USUARIO

# LISTAR 
@login_required
@GrupoCooperativos('EjecutivoAdministrador','admin')
def listadoTipoUsuario(request):
    tipoUsuarios = TipoUsuario.objects.all()
    page = request.GET.get('page',1)

    try:
        paginator = Paginator(tipoUsuarios,6)
        tipoUsuarios = paginator.page(page)
    except:
        raise Http404
        
    aux = {
        'entity' : tipoUsuarios,
        'paginator': paginator
    }
    return render(request,'core/administracion/tipoUsuario/tipoUsuarioLista.html',aux)
# AGREGAR
@login_required
@GrupoCooperativos('EjecutivoAdministrador','admin')
def agregarTipoUsuario(request):
    aux = {
        'form': TipoUsuarioForm()
    }
    if request.method == 'POST':
        formulario = TipoUsuarioForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"TIPO USUARIO AGREGADO CORRECTAMENTE")
            return redirect(to="listadoTipoUsuario")
        else:
            aux['form'] = formulario

    return render(request,'core/administracion/tipoUsuario/tipoUsuarioAgregar.html',aux)
# ACTUALIZAR
@login_required
@GrupoCooperativos('EjecutivoAdministrador','admin')
def actualizarTipoUsuario(request,id):
    usuario = TipoUsuario.objects.get(id=id)
    aux = {
        'form': TipoUsuarioForm(instance=usuario)
    }
    if request.method == 'POST':
        formulario = TipoUsuarioForm(request.POST,instance=usuario)
        if formulario.is_valid():
            formulario.save()
            aux['form'] = formulario
            messages.success(request,"TIPO DE USUARIO ACTUALIZADO CORRECTAMENTE")
            return redirect(to="listadoTipoUsuario")
        else:
            aux['form'] = formulario   

    return render(request,'core/administracion/tipoUsuario/tipoUsuarioActualizar.html',aux)
# ELIMINAR
@login_required
@GrupoCooperativos('EjecutivoAdministrador','admin')
def eliminarTipoUsuario(request,id):
    usuario = TipoUsuario.objects.get(id=id)
    usuario.delete()
    messages.success(request,"TIPO DE USUARIO ELIMINADO CORRECTAMENTE")
    return redirect(to="listadoTipoUsuario")




#CRUD TIPO OBRA
#LISTA
@login_required
@GrupoCooperativos('EjecutivoAdministrador','admin')
def listadoTipoObra(request):
    tipoObra = TipoObra.objects.all()
    page = request.GET.get('page',1)

    try:
        paginator = Paginator(tipoObra,6)
        tipoObra = paginator.page(page)
    except:
        raise Http404
        
    aux = {
        'entity' : tipoObra,
        'paginator': paginator
    }
    return render(request,'core/administracion/tipoObras/tipoObraLista.html',aux)
# AGREGAR
@login_required
@GrupoCooperativos('EjecutivoAdministrador','admin')
def agregarTipoObra(request):
    aux = {
        'form': TipoObraForm()
    }
    if request.method == 'POST':
        formulario = TipoObraForm(data=request.POST,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"TIPO DE OBRA AGREGADA CORRECTAMENTE")
            return redirect(to="listadoTipoObra")
        else:
            aux['form'] = formulario

    return render(request,'core/administracion/tipoObras/tipoObraAgregar.html',aux)
# ACTUALIZAR
@login_required
@GrupoCooperativos('EjecutivoAdministrador','admin')
def actualizarTipoObra(request,id):
    usuario = TipoObra.objects.get(id=id)
    aux = {
        'form': TipoObraForm(instance=usuario)
    }
    if request.method == 'POST':
        formulario = TipoObraForm(request.POST,instance=usuario)
        if formulario.is_valid():
            formulario.save()
            aux['form'] = formulario
            messages.success(request,"TIPO DE OBRA ACTUALIZADA CORRECTAMENTE")
            return redirect(to="listadoTipoObra")
        else:
            aux['form'] = formulario   

    return render(request,'core/administracion/tipoObras/tipoObraActualizar.html',aux)
# ELIMINAR
@login_required
@GrupoCooperativos('EjecutivoAdministrador','admin')
def eliminarTipoObra(request,id):
    usuario = TipoObra.objects.get(id=id)
    usuario.delete()
    messages.success(request,"TIPO DE OBRA ELIMINADA CORRECTAMENTE")
    return redirect(to="listadoTipoObra")





# CRUD OBRAS
#LISTAR
@login_required
@GrupoCooperativos('EjecutivoAdministrador','admin')
def listadoObras(request):
    Obras = Obra.objects.all()
    page = request.GET.get('page',1)

    try:
        paginator = Paginator(Obras,6)
        Obras = paginator.page(page)
    except:
        raise Http404
        
    aux = {
        'entity' : Obras,
        'paginator': paginator
    }
    return render(request,'core/administracion/obras/obraLista.html',aux)
# AGREGAR
@login_required
def agregarObras(request):
    if request.method == 'POST':
        form = ObraForm(request.POST, files=request.FILES)
        if form.is_valid():
            obra = form.save(commit=False)
            obra.NombreUsuario = request.user.username
            obra.save()
            messages.success(request, "OBRA AGREGADA CORRECTAMENTE")
            return redirect('CuentaCooperativos')
    else:
        current_date_time = datetime.now().strftime('%Y%m%d_%H%M%S')
        default_code = f"{request.user.username}_{current_date_time}"
        form = ObraForm(initial={
            'NombreUsuario': request.user.username,
            'codigo': default_code,
            'fechaIngreso': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })

    context = {
        'form': form,
        }
    return render(request, 'core/administracion/obras/obraAgregar.html', context)
#ACTUALIZAR
@login_required
@GrupoCooperativos('EjecutivoAdministrador','admin')
def actualizarObras(request,id):
    usuario = Obra.objects.get(id=id)
    aux = {
        'form': ObraForm(instance=usuario)
    }
    if request.method == 'POST':
        formulario = ObraForm(request.POST,instance=usuario,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            aux['form'] = formulario
            messages.success(request,"OBRA ACTUALIZADA CORRECTAMENTE")
            return redirect(to="listadoObras")
        else:
            aux['form'] = formulario   

    return render(request,'core/administracion/obras/obraActualizar.html',aux)
# ELIMINAR
@login_required
@GrupoCooperativos('EjecutivoAdministrador','admin')
def eliminarObras(request,id):
    usuario = Obra.objects.get(id=id)
    usuario.delete()
    messages.success(request,"OBRA ELIMINADA CORRECTAMENTE")
    return redirect(to="listadoObras")










# CRUD SOLICITUD OBRA
#LISTAR
@login_required
@GrupoCooperativos('EjecutivoAdministrador','admin')
def listadoSolicitudObra(request):
    Solicitudes = SolicitudObra.objects.all()
    page = request.GET.get('page',1)

    try:
        paginator = Paginator(Solicitudes,6)
        Solicitudes = paginator.page(page)
    except:
        raise Http404
        
    aux = {
        'entity' : Solicitudes,
        'paginator': paginator
    }
    return render(request,'core/administracion/solicitudes/solicitudLista.html',aux)
# AGREGAR
@login_required
@GrupoCooperativos('EjecutivoAdministrador','admin')
def agregarSolicitudObra(request):
    aux = {
        'form': SolicitudObraForm()
    }
    if request.method == 'POST':
        formulario = SolicitudObraForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"ESTADO DE SOLICITUD OBRA AGREGADA CORRECTAMENTE")
            return redirect(to="listadoSolicitudObra")
        else:
            aux['form'] = formulario

    return render(request,'core/administracion/solicitudes/solicitudAgregar.html',aux)
#ACTUALIZAR
@login_required
@GrupoCooperativos('EjecutivoAdministrador','admin')
def actualizarSolicitudObra(request,id):
    usuario = SolicitudObra.objects.get(id=id)
    aux = {
        'form': SolicitudObraForm(instance=usuario)
    }
    if request.method == 'POST':
        formulario = SolicitudObraForm(data=request.POST,instance=usuario)
        if formulario.is_valid():
            formulario.save()
            aux['form'] = formulario
            messages.success(request,"ESTADO DE SOLICITUD OBRA ACTUALIZADA CORRECTAMENTE")
            return redirect(to="listadoSolicitudObra")
        else:
            aux['form'] = formulario   

    return render(request,'core/administracion/solicitudes/solicitudActualizar.html',aux)
# ELIMINAR
@login_required
@GrupoCooperativos('EjecutivoAdministrador','admin')
def eliminarSolicitudObra(request,id):
    usuario = SolicitudObra.objects.get(id=id)
    usuario.delete()
    messages.success(request,"ESTADO DE SOLICITUD OBRA ELIMINADA CORRECTAMENTE")
    return redirect(to="listadoSolicitudObra")


# CRUD AUTENTIFICACION
def agregarAutentificacion(request):
    aux = {
        'form': AutentificacionForm(),
        'cuentasAutentificadas': None,
    }
    if request.method == 'POST':
        formulario = AutentificacionForm(data=request.POST,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            cliente_group, created = Group.objects.get_or_create(name='ClientesAutentificados')
            request.user.groups.add(cliente_group)

            no_cliente_group, created = Group.objects.get_or_create(name='ClientesNoAutentificados')
            if no_cliente_group in request.user.groups.all():
                request.user.groups.remove(no_cliente_group)


            messages.success(request," AUTENTIFICACION AGREGADA CORRECTAMENTE")
            return render(request,'core/inicio.html',aux)
        else:
            aux['form'] = formulario
    if request.user.is_authenticated:
        aux['cuentasAutentificadas'] = Autentificacion.objects.all()
    return render(request,'core/cliente.html',aux)


# CRUD CUENTA
#LISTAR
@login_required
@GrupoCooperativos('EjecutivoAdministrador','admin')
def listadoCuentas(request):
    cuentas = Cuenta.objects.all()
    page = request.GET.get('page',1)

    try:
        paginator = Paginator(cuentas,6)
        cuentas = paginator.page(page)
    except:
        raise Http404
        
    aux = {
        'entity' : cuentas,
        'paginator': paginator
    }
    return render(request,'core/administracion/cuentas/cuentaLista.html',aux)
# AGREGAR
@login_required
@GrupoCooperativos('EjecutivoAdministrador','admin')
def agregarCuentas(request):
    aux = {
        'form': CuentaForm()
    }
    if request.method == 'POST':
        formulario = CuentaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"CUENTA AGREGADA CORRECTAMENTE")
            return redirect(to="listadoCuentas")
        else:
            aux['form'] = formulario

    return render(request,'core/administracion/cuentas/cuentaAgregar.html',aux)
#ACTUALIZAR
@login_required
@GrupoCooperativos('EjecutivoAdministrador','admin')
def actualizarCuentas(request,id):
    usuario = Cuenta.objects.get(id=id)
    aux = {
        'form': CuentaForm(instance=usuario)
    }
    if request.method == 'POST':
        formulario = CuentaForm(request.POST,instance=usuario)
        if formulario.is_valid():
            formulario.save()
            aux['form'] = formulario
            messages.success(request,"CUENTA ACTUALIZADA CORRECTAMENTE")
            return redirect(to="listadoCuentas")
        else:
            aux['form'] = formulario   

    return render(request,'core/administracion/cuentas/cuentaActualizar.html',aux)
# ELIMINAR
@login_required
@GrupoCooperativos('EjecutivoAdministrador','admin')
def eliminarCuentas(request,id):
    usuario = Cuenta.objects.get(id=id)
    usuario.delete()
    messages.success(request,"CUENTA ELIMINADA CORRECTAMENTE")
    return redirect(to="listadoCuentas")



# CRUD COMPRA
#LISTAR
@login_required
@GrupoCooperativos('EjecutivoAdministrador','admin')
def listadoCompra(request):
    Compras = Compra.objects.all()
    page = request.GET.get('page',1)

    try:
        paginator = Paginator(Compras,6)
        Compras = paginator.page(page)
    except:
        raise Http404
        
    aux = {
        'entity' : Compras,
        'paginator': paginator
    }
    return render(request,'core/administracion/compras/compraLista.html',aux)
# AGREGAR
@login_required
def agregarCompra(request):
    aux = {
        'form': ObraForm()
    }
    if request.method == 'POST':
        formulario = CompraForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"COMPRA AGREGADA AL CARRITO")
            return redirect(to="carroCompra")
        else:
            aux['form'] = formulario

    return render(request,'core/administracion/compras/compraAgregar.html',aux)
#ACTUALIZAR
@login_required
@GrupoCooperativos('EjecutivoAdministrador','admin')
def actualizarCompra(request,id):
    usuario = Compra.objects.get(id=id)
    aux = {
        'form': CompraForm(instance=usuario)
    }
    if request.method == 'POST':
        formulario = CompraForm(request.POST,instance=usuario)
        if formulario.is_valid():
            formulario.save()
            aux['form'] = formulario
            messages.success(request,"COMPRA ACTUALIZADA CORRECTAMENTE")
            return redirect(to="listadoCompra")
        else:
            aux['form'] = formulario   

    return render(request,'core/administracion/compras/compraActualizar.html',aux)
# ELIMINAR
@login_required
def eliminarCompra(request,id):
    obraCarrito = Compra.objects.get(id=id)
    obraCarrito.delete()
    messages.success(request,"ARTICULO ELIMINADO CORRECTAMENTE")
    return redirect(to="compra")







# REGISTRAR CUENTA
def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method== 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(user=formulario.cleaned_data["username"],password= formulario.cleaned_data["password1"])
            usuarioIngreso = User.objects.get(username = formulario.cleaned_data["username"])
            group = Group.objects.get(name='clientes')
            usuarioIngreso.groups.add(group)
            group = Group.objects.get(name='ClientesNoAutentificados')
            usuarioIngreso.groups.add(group)
            login(user)
            return redirect(to="inicio")
        data["form"] = formulario
    return render(request,'registration/registro.html',data)





#CONSULTA DE DETALLE
def detalleObra(request,id):
    usuario = Obra.objects.filter(id=id)
    aux = {
        'lista': usuario
    }
    return render(request,'core/informacionCompra.html',aux)