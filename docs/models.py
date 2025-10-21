from django.db import models

# Create your models here.
class Directores(models.Model):
    id_dir = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=False, blank=False, verbose_name="Nombre")
    rut = models.CharField(max_length=10, null=False, blank=False, unique=True, verbose_name="RUT")
    seg_nombre = models.CharField(max_length=100, null=True, blank=True, verbose_name="Segundo Nombre")
    apellido_p = models.CharField(max_length=100, null=False, blank=False, verbose_name="Apellido Paterno")
    apellido_m = models.CharField(max_length=100, null=False, blank=False, verbose_name="Apellido Materno")
    email = models.EmailField(max_length=100, null=False, blank=False, unique=True, verbose_name="Correo Electrónico")
    telefono = models.CharField(max_length=10, null=True, blank=True, verbose_name="Teléfono")

    class Meta:
        verbose_name = 'Director'
        verbose_name_plural = 'Directores'

    def __str__(self):
        return f"{self.nombre} {self.apellido_p} {self.apellido_m}"

class Comunas(models.Model):
    id_comuna = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=False, blank=False)

    class Meta:
        verbose_name = 'Comuna'
        verbose_name_plural = 'Comunas'

    def __str__(self):
        return f"{self.nombre}"    


class Establecimientos(models.Model):
    id_est = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=False, blank=False)
    rbd = models.CharField(max_length=10, null=False, blank=False)
    direccion = models.CharField(max_length=100, null=False, blank=False)
    comuna = models.ForeignKey(Comunas, on_delete=models.SET_NULL, null=True, related_name='establecimientos')
    email = models.EmailField(max_length=100, null=False, blank=False, unique=True)
    director = models.ForeignKey(Directores, on_delete=models.SET_NULL, null=True, related_name='establecimientos')
    activo = models.BooleanField(default=True, verbose_name="Activo")

    class Meta:
        verbose_name = 'Establecimiento'
        verbose_name_plural = 'Establecimientos'
        unique_together = ['rbd', 'nombre']

    def __str__(self):
        return f"{self.nombre} ({self.rbd}) ({self.comuna})"


class TipoProveedor(models.Model):
    id_tipo_prov = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=False, blank=False, verbose_name="Tipo de Proveedor")
    

    class Meta:
        verbose_name = 'Tipo de Proveedor'
        verbose_name_plural = 'Tipos de Proveedores'

    def __str__(self):
        return self.nombre

class Proveedor(models.Model):
    id_prov = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=False, blank=False, verbose_name="Nombre")
    rut = models.CharField(max_length=10, null=False, blank=False, unique=True, verbose_name="RUT")
    tipo_proveedor = models.ForeignKey(TipoProveedor, on_delete=models.CASCADE, related_name='proveedores')
    acronimo = models.CharField(max_length=10, null=False, blank=False, verbose_name="Acrónimo", default='ADA')

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'

    def __str__(self):
        return self.nombre

class TipoRecibo(models.Model):
    id_tipo_rec = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=False, blank=False, verbose_name="Tipo de Recibo")
    

    class Meta:
        verbose_name = 'Tipo de Recibo'
        verbose_name_plural = 'Tipos de Recibos'

    def __str__(self):
        return self.nombre


class Servicios(models.Model):
    id_serv = models.AutoField(primary_key=True)
    numero_servicio = models.CharField(max_length=100, null=False, blank=False, verbose_name="Número de Servicio")
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name='servicios')
    establecimiento = models.ForeignKey(Establecimientos, on_delete=models.CASCADE, related_name='servicios')
    tipo_recibo = models.ForeignKey(TipoRecibo, on_delete=models.CASCADE, related_name='servicios')

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        unique_together = ['numero_servicio', 'proveedor', 'establecimiento']

    def __str__(self):
        return f"Servicio {self.numero_servicio} - {self.establecimiento}"


class RegistroServicio(models.Model):
    id_registro = models.AutoField(primary_key=True)
    servicio = models.ForeignKey(Servicios, on_delete=models.CASCADE, related_name='registros')
    numero_recibo = models.CharField(max_length=100, null=False, blank=False, verbose_name="Número de Factura o Boleta")
    fecha_envio_pago = models.DateField(null=False, blank=False, verbose_name="Fecha de Envío a Pago")
    fecha_emision = models.DateField(null=True, blank=True, verbose_name="Fecha de Emisión")
    fecha_vencimiento = models.DateField(null=False, blank=False, verbose_name="Fecha de Vencimiento")
    interes = models.IntegerField(null=True, blank=True, default=0, verbose_name="Interés")
    monto = models.IntegerField(null=False, blank=False, verbose_name="Monto")

    class Meta:
        verbose_name = 'Registro de Servicio'
        verbose_name_plural = 'Registros de Servicios'
        unique_together = ['servicio', 'numero_recibo']

    def __str__(self):
        return f"Registro {self.numero_recibo} - {self.servicio}"

