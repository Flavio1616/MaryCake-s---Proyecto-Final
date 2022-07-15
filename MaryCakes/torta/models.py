from django.db import models

# Create your models here.
class Torta(models.Model):
    title = models.CharField(max_length=200, verbose_name= "Título")
    description = models.TextField(verbose_name= "Descripción")
    image = models.ImageField(verbose_name= "Imagen")
    created = models.DateTimeField(auto_now_add=True, verbose_name= "Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name= "Fecha de Edición")
    class Meta:
        verbose_name = 'torta'
        verbose_name_plural = 'tortas'
        ordering = ["-created"]
    def _str_(self):
        return self.title
