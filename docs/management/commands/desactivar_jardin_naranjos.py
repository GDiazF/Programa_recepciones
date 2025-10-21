from django.core.management.base import BaseCommand
from docs.models import Establecimientos

class Command(BaseCommand):
    help = 'Marca el Jardín Infantil Los Naranjos como inactivo'

    def handle(self, *args, **options):
        try:
            # Buscar el jardín por nombre
            jardin = Establecimientos.objects.get(nombre__icontains='los naranjos')
            jardin.activo = False
            jardin.save()
            
            self.stdout.write(
                self.style.SUCCESS(
                    f'[OK] Jardin "{jardin.nombre}" marcado como inactivo exitosamente'
                )
            )
        except Establecimientos.DoesNotExist:
            self.stdout.write(
                self.style.WARNING(
                    '[WARNING] No se encontró un jardín con "Los Naranjos" en el nombre'
                )
            )
        except Establecimientos.MultipleObjectsReturned:
            jardines = Establecimientos.objects.filter(nombre__icontains='los naranjos')
            self.stdout.write(
                self.style.WARNING(
                    f'[WARNING] Se encontraron múltiples jardines con "Los Naranjos": {[j.nombre for j in jardines]}'
                )
            )
            self.stdout.write(
                'Por favor, especifica el nombre exacto o usa el admin de Django para marcar el correcto como inactivo.'
            )
