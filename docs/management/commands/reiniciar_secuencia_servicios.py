from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Reinicia la secuencia de IDs de la tabla de servicios a 1'

    def handle(self, *args, **options):
        try:
            with connection.cursor() as cursor:
                # Reiniciar la secuencia de la tabla docs_servicios
                cursor.execute("ALTER SEQUENCE docs_servicios_id_serv_seq RESTART WITH 1")
                self.stdout.write(self.style.SUCCESS('Secuencia de IDs reiniciada exitosamente'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error al reiniciar la secuencia: {str(e)}')) 