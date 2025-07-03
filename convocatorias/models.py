from django.db import models

class Cursos(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del Curso")
    descripcion = models.TextField(verbose_name="Descripción")
    duracion_horas = models.IntegerField(verbose_name="Duración (horas)")
    costo = models.FloatField(verbose_name="Costo del Curso", default=0.0)  # NUEVO CAMPO
    activo = models.BooleanField(default=True, verbose_name="¿Está activo?")
    imagen = models.ImageField(upload_to="cursos/", null=True, blank=True, verbose_name="Imagen del Curso")
    creado_en = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    actualizado_en = models.DateTimeField(auto_now=True, verbose_name="Última actualización")

    
    class Meta:
        verbose_name = "Cursos"
        verbose_name_plural = "Cursos"
        ordering = ["creado_en"]

    def __str__(self):
        return self.nombre

# Create your models here.
