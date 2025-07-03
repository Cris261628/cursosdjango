from django.contrib import admin
from .models import Cursos

class Administrarcursos(admin.ModelAdmin):
    readonly_fields = ('creado_en', 'actualizado_en')
    list_display = ('nombre', 'duracion_horas', 'activo', 'creado_en')
    search_fields = ('nombre', 'descripcion')
    date_hierarchy = 'creado_en'
    list_filter = ('activo',)

    
admin.site.register(Cursos, Administrarcursos)
