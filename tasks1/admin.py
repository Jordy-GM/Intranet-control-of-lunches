from django.contrib import admin  # Importa el módulo de administración de Django.
from .models import Task, Menu, Menuselection  # Importa el modelo Task desde el archivo models.py del mismo directorio.

# Register your models here.

class TaskAdmin(admin.ModelAdmin):  # Define una clase de configuración para personalizar la administración del modelo Task.
    readonly_fields = ("created",)  # Especifica que el campo 'created' será de solo lectura en el panel de administración.

admin.site.register(Task, TaskAdmin)  # Registra el modelo Task en el sitio de administración para que pueda ser gestionado desde el admin de Django.
                                      # Registra el modelo Task en el sitio de administración utilizando la configuración personalizada de TaskAdmin.



# Registra el modelo Menu en el sitio de administración.
admin.site.register(Menu)  # Registro simple, usando la configuración predeterminada.

# Registra el modelo Menuselection en el sitio de administración.
admin.site.register(Menuselection)  # Registro simple, usando la configuración predeterminada.