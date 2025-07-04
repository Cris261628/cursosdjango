from django.contrib import admin
from .models import Cursos, Actividad


class Administrarcursos(admin.ModelAdmin):
    readonly_fields = ('creado_en', 'actualizado_en')
    list_display = ('nombre', 'duracion_horas', 'activo', 'creado_en')
    search_fields = ('nombre', 'descripcion')
    date_hierarchy = 'creado_en'
    list_filter = ('activo',)

    
admin.site.register(Cursos, Administrarcursos)


class AdministrarActividad(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion',)
    list_display = ('clave', 'curso', 'fecha_creacion')
    search_fields = ('clave', 'descripcion', 'curso__nombre')
    list_filter = ('curso',)
    fieldsets = (
        ("Información de la Actividad", {
            'fields': ('curso', 'clave', 'descripcion')
        }),
        ("Datos del sistema", {
            'fields': ('fecha_creacion',),
            'classes': ('collapse',)
        }),
    )

admin.site.register(Actividad, AdministrarActividad)