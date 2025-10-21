from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Establecimientos)
class EstablecimientosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'rbd', 'comuna', 'director', 'activo', 'email')
    list_filter = ('activo', 'comuna', 'director')
    search_fields = ('nombre', 'rbd', 'email')
    list_editable = ('activo',)
    ordering = ('nombre',)

admin.site.register(Directores)
admin.site.register(TipoProveedor)
admin.site.register(Proveedor)
admin.site.register(TipoRecibo)
admin.site.register(Servicios)
admin.site.register(Comunas)
admin.site.register(RegistroServicio)
