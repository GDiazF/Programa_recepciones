import pandas as pd
from django.core.management.base import BaseCommand
from docs.models import Servicios, Establecimientos, Proveedor, TipoRecibo

class Command(BaseCommand):
    help = 'Importa servicios desde un archivo Excel'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Ruta del archivo Excel')

    def handle(self, *args, **options):
        file_path = options['file_path']
        
        try:
            # Leer el archivo Excel
            df = pd.read_excel(file_path)
            
            # Contador para estadísticas
            total = 0
            exitosos = 0
            fallidos = 0
            
            for index, row in df.iterrows():
                total += 1
                try:
                    # Obtener el establecimiento por RBD
                    establecimiento = Establecimientos.objects.get(rbd=row['rbd'])
                    
                    # Obtener el proveedor por RUT
                    proveedor = Proveedor.objects.get(rut=row['rut_proveedor'])
                    
                    # Obtener el tipo de recibo por nombre
                    tipo_recibo = TipoRecibo.objects.get(nombre=row['tipo_recibo'])
                    
                    # Crear el servicio
                    servicio = Servicios.objects.create(
                        numero_servicio=row['numero_servicio'],
                        proveedor=proveedor,
                        establecimiento=establecimiento,
                        tipo_recibo=tipo_recibo
                    )
                    
                    exitosos += 1
                    self.stdout.write(self.style.SUCCESS(f'Importado servicio {servicio.numero_servicio} para {establecimiento.nombre}'))
                    
                except Exception as e:
                    fallidos += 1
                    self.stdout.write(self.style.ERROR(f'Error en fila {index + 2}: {str(e)}'))
            
            # Mostrar estadísticas
            self.stdout.write(self.style.SUCCESS(f'''
                Importación completada:
                Total: {total}
                Exitosos: {exitosos}
                Fallidos: {fallidos}
            '''))
            
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error al procesar el archivo: {str(e)}')) 