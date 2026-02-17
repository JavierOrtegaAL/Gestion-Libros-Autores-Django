from django.db import models


def upload_image(instance, filename):
    if instance.pk:
        old_instance=Autor.objects.get(pk=instance.pk)
        if old_instance.foto.name=='libros/'+filename:
            old_instance.foto.delete()
    return 'libros/media/libros/'+filename
    
# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=50)
    foto = models.ImageField(upload_to=upload_image,null=True, blank=True)
    descripcion=models.TextField(max_length=1000,null=True,blank=True)
    class Meta:
        verbose_name="Autor"
        verbose_name_plural="Autores"
        ordering=["nombre","nacionalidad"]
    def __str__(self):
        return self.nombre


class Libro(models.Model):
    titulo = models.CharField(max_length=50)
    fecha_publicacion = models.IntegerField("Año de publicación")
    disponible = models.BooleanField(default=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    descripcion=models.TextField(max_length=1000,null=True,blank=True)
    class Meta:
        verbose_name="Libro"
        verbose_name_plural="Libros"
        ordering=["titulo","autor","fecha_publicacion"]
