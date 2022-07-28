from django.db import models

# Create your models here.
class Torta(models.Model):
    idtorta = models.AutoField(primary_key=True)
    title = models.CharField(blank=False, null=False, max_length=200, verbose_name= "Nombre del producto")
    tipo = models.CharField(blank=False, null=False, max_length=50, default="null", verbose_name="Tipo")
    form_torta = models.CharField(blank=False, null=False, max_length=100, default="null", verbose_name="Forma")
    weight = models.FloatField(blank=False, null=False, default=0.0, verbose_name="Peso en Kilogramos")
    coste_fabri = models.FloatField(blank=False, null=False, default=0.0, verbose_name="Coste de fabricación")
    coste = models.FloatField(blank=False, null=False, default=0.0, verbose_name="Valor final")
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

class Postres(models.Model):
    idPostres = models.AutoField(primary_key=True)
    title = models.CharField(blank=False, null=False, max_length=200, verbose_name= "Nombre del producto")
    tipo = models.CharField(blank=False, null=False, max_length=50, default="null", verbose_name="Tipo")
    amount_box = models.SmallIntegerField(blank=False, null=False, default=0, verbose_name="Cantidad por paquete")
    coste_fabri = models.FloatField(blank=False, null=False, default=0.0, verbose_name="Coste de fabricación")
    coste = models.FloatField(blank=False, null=False, default=0.0, verbose_name="Valor final")
    description = models.TextField(blank=False, null=False, verbose_name= "Descripción")
    image = models.ImageField(verbose_name= "Imagen")
    created = models.DateTimeField(auto_now_add=True, verbose_name= "Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name= "Fecha de Edición")

    class Meta:
        verbose_name = 'postre'
        verbose_name_plural = 'postres'
        ordering = ["-created"]
    def _str_(self):
        return self.title
