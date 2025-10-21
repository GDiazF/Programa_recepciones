from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'docs'  # Namespace para las URLs de la aplicación

urlpatterns = [
    path('', login_required(views.base), name='base'),
    path('dashboard/', login_required(views.dashboard), name='dashboard'),
    path('proximos-vencer/', login_required(views.proximos_vencer), name='proximos_vencer'),
    path('reportes-periodo/', login_required(views.reportes_periodo), name='reportes_periodo'),
    path('exportar-reporte-periodo/', login_required(views.exportar_reporte_periodo), name='exportar_reporte_periodo'),
    
    # URLs de Establecimientos
    path('establecimientos/', login_required(views.listar_establecimientos), name='listar_establecimientos'),
    path('establecimiento/crear/', login_required(views.crear_establecimiento), name='crear_establecimiento'),
    path('establecimiento/<int:id_est>/', login_required(views.ver_establecimiento), name='ver_establecimiento'),
    path('establecimiento/editar/<int:establecimiento_id>/', login_required(views.editar_establecimiento), name='editar_establecimiento'),
    path('establecimiento/eliminar/<int:establecimiento_id>/', login_required(views.eliminar_establecimiento), name='eliminar_establecimiento'),
    path('establecimiento/toggle-activo/<int:establecimiento_id>/', login_required(views.toggle_establecimiento_activo), name='toggle_establecimiento_activo'),
    
    # URLs de Servicios
    path('servicios/', login_required(views.listar_servicios), name='listar_servicios'),
    path('servicio/crear/', login_required(views.crear_servicio), name='crear_servicio'),
    path('servicio/<int:servicio_id>/', login_required(views.ver_servicio), name='ver_servicio'),
    path('servicio/editar/<int:servicio_id>/', login_required(views.editar_servicio), name='editar_servicio'),
    path('servicio/eliminar/<int:servicio_id>/', login_required(views.eliminar_servicio), name='eliminar_servicio'),
    
    # URLs de Registros
    path('registros/', login_required(views.listar_registros), name='listar_registros'),
    path('descargar-pdfs-jardines/', login_required(views.descargar_pdfs_jardines), name='descargar_pdfs_jardines'),
    path('descargar-zip-jardines/', login_required(views.descargar_zip_jardines), name='descargar_zip_jardines'),
    path('registro/crear/', login_required(views.crear_registro), name='crear_registro'),
    path('registro/buscar/', login_required(views.buscar_registro), name='buscar_registro'),
    path('registro/editar/<int:registro_id>/', login_required(views.editar_registro), name='editar_registro'),
    path('registro/enviar-correo/<int:registro_id>/', login_required(views.generar_enlace_correo), name='generar_enlace_correo'),
    path('registro/importar/', login_required(views.importar_registros), name='importar_registros'),
    path('registro/plantilla/', login_required(views.descargar_plantilla_registros), name='descargar_plantilla_registros'),
    path('registro/descargar_masivo_registro/', login_required(views.descargarMasivoRegistros), name='descargar_masivo_registro'),
    path('registro/pdf/<int:registro_id>/', login_required(views.descargar_registro_pdf), name='descargar_registro_pdf'),
    
    # URLs de Usuario
    path('perfil/', login_required(views.perfil_usuario), name='perfil_usuario'),
    path('cambiar-password/', login_required(views.CambiarPasswordView.as_view()), name='cambiar_password'),
    
    # URLs de Procesar Planillas
    path('procesar-planillas/', login_required(views.procesar_planillas), name='procesar_planillas'),
] 