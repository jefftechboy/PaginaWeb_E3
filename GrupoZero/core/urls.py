from django.urls import path,include
from .views import *
from rest_framework import routers
from .serializers import *

router = routers.DefaultRouter()
router.register('Comuna', ComunaViewSet)
router.register('TipoUsuario', TipoUsuarioViewSet)
router.register('Region', RegionViewSet)
router.register('Cuenta', CuentaViewSet)
router.register('Usuario', UsuarioViewSet)
router.register('TipoObra', TipoObraViewSet)
router.register('SolicitudObra', SolicitudObraViewSet)
router.register('Obra', ObraViewSet)
router.register('EstadoCompra', EstadoCompraViewSet)
router.register('Autentificacion', AutentificacionViewSet)
router.register('ComTipoBancopra', TipoBancoViewSet)
router.register('TipoCuenta', TipoCuentaViewSet)
router.register('DatosCooperativos', DatosCooperativosViewSet)

urlpatterns = [
    path('api/', include(router.urls)),

    path('',inicio),
    path('inicio/',inicio,name="inicio"),

    path('account_locked/',account_locked,name="account_locked"),
    path('login/',login,name="login"),

    
    path('tienda/',tienda,name="tienda"),
    path('pago/',pago,name="pago"),
    path('carroCompra/',carroCompra,name="compra"),
    path('contacto/',contacto,name="contacto"),
    path('equipo/',equipo,name="equipo"),
    path('detalleObra/<id>/',detalleObra,name="detalleObra"),
    path('404/',error404,name="404"),
    path('administracion/',administracion,name="administracion"),
    path('registro/',registro,name="registro"),
    path('informacioncompra/', informacionCompra, name='informacionCompra'),



    

    # LISTA CUENTA COOPERATIVO
    path('CuentaCooperativos/',CuentaCooperativos,name="CuentaCooperativos"),
    



    #CRUD Datos Cooperativos
    path('DatosCuentaCooperativo/',DatosCuentaCooperativo,name="DatosCuentaCooperativo"),
    path('actualizarDatosCooperativos/<id>/',actualizarDatosCooperativos,name="actualizarDatosCooperativos"),
    path('agregarDatosCooperativos/',agregarDatosCooperativos,name="agregarDatosCooperativos"),
    path('agregarDatosCooperativos/eliminarDatosCooperativos/<id>/',eliminarDatosCooperativos,name="eliminarDatosCooperativos"),
    
    #CRUD TIPO BANCOS
    path('listadoTipoBanco/',listadoTipoBanco,name="listadoTipoBanco"),
    path('actualizarTipoBanco/<id>/',actualizarTipoBanco,name="actualizarTipoBanco"),
    path('agregarTipoBanco/',agregarTipoBanco,name="agregarTipoBanco"),
    path('agregarTipoBanco/eliminarTipoBanco/<id>/',eliminarTipoBanco,name="eliminarTipoBanco"),
    

    #CRUD TIPO CUENTAS BANCARIAS
    path('listadoTipoCuentas/',listadoTipoCuentas,name="listadoTipoCuentas"),
    path('actualizarTipoCuentas/<id>/',actualizarTipoCuentas,name="actualizarTipoCuentas"),
    path('agregarTipoCuentas/',agregarTipoCuentas,name="agregarTipoCuentas"),
    path('agregarTipoCuentas/eliminarTipoCuentas/<id>/',eliminarTipoCuentas,name="eliminarTipoCuentas"),
    


    #CRUD AUTENTIFICACION
    path('cuentaCliente/',agregarAutentificacion,name="cuentaCliente"),
    
    
    
    # CRUD USUARIOS
    path('listado/',listado,name="listado"),
    path('update/<id>/',update,name="update"),
    path('ad/',ad,name="ad"),
    path('ad/delete/<id>/',delete,name="delete"),
    # CRUD TIPO USUARIOS
    path('listadoTipoUsuario/',listadoTipoUsuario,name="listadoTipoUsuario"),
    path('agregarTipoUsuario/',agregarTipoUsuario,name="agregarTipoUsuario"),
    path('actualizarTipoUsuario/<id>/',actualizarTipoUsuario,name="actualizarTipoUsuario"),
    path('agregarTipoUsuario/eliminarTipoUsuario/<id>/',eliminarTipoUsuario,name="eliminarTipoUsuario"),
    #CRUD TIPO OBRA
    path('listadoTipoObra/',listadoTipoObra,name="listadoTipoObra"),
    path('agregarTipoObra/',agregarTipoObra,name="agregarTipoObra"),
    path('actualizarTipoObra/<id>/',actualizarTipoObra,name="actualizarTipoObra"),
    path('agregarTipoObra/eliminarTipoObra/<id>/',eliminarTipoObra,name="eliminarTipoObra"),
    #CRUD OBRA
    path('listadoObras/',listadoObras,name="listadoObras"),
    path('agregarObras/',agregarObras,name="agregarObras"),
    path('actualizarObras/<id>/',actualizarObras,name="actualizarObras"),
    path('agregarObras/eliminarObras/<id>/',eliminarObras,name="eliminarObras"),
    #CRUD SOLICITUD OBRA
    path('listadoSolicitudObra/',listadoSolicitudObra,name="listadoSolicitudObra"),
    path('agregarSolicitudObra/',agregarSolicitudObra,name="agregarSolicitudObra"),
    path('actualizarSolicitudObra/<id>/',actualizarSolicitudObra,name="actualizarSolicitudObra"),
    path('agregarSolicitudObra/eliminarSolicitudObra/<id>/',eliminarSolicitudObra,name="eliminarSolicitudObra"),
    #CRUD CUENTA
    path('listadoCuentas/',listadoCuentas,name="listadoCuentas"),
    path('agregarCuentas/',agregarCuentas,name="agregarCuentas"),
    path('actualizarCuentas/<id>/',actualizarCuentas,name="actualizarCuentas"),
    path('agregarCuentas/eliminarCuentas/<id>/',eliminarCuentas,name="eliminarCuentas"),
    #CRUD COMPRA
    path('listadoCompra/',listadoCompra,name="listadoCompra"),
    path('agregarCompra/',agregarCompra,name="agregarCompra"),
    path('actualizarCompra/<id>/',actualizarCompra,name="actualizarCompra"),
    path('agregarCompra/eliminarCompra/<id>/',eliminarCompra,name="eliminarCompra"),
    #CRUD COMUNA
    path('listadoComuna/',listadoComuna,name="listadoComuna"),
    path('agregarComuna/',agregarComuna,name="agregarComuna"),
    path('actualizarComuna/<id>/',actualizarComuna,name="actualizarComuna"),
    path('agregarComuna/eliminarComuna/<id>/',eliminarComuna,name="eliminarComuna"),
    #CRUD REGION
    path('listadoRegion/',listadoRegion,name="listadoRegion"),
    path('agregarRegion/',agregarRegion,name="agregarRegion"),
    path('actualizarRegion/<id>/',actualizarRegion,name="actualizarRegion"),
    path('agregarRegion/eliminarRegion/<id>/',eliminarRegion,name="eliminarRegion"),



]

