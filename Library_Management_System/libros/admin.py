from django.contrib import admin

from libros.models import Autor, Libro

# Register your models here.
class AutorAdmin(admin.ModelAdmin):
    list_display = ("nombre","nacionalidad")
    ordering = ("nombre", "nacionalidad")
    search_fields = ("nombre", "nacionalidad")
    list_filter = ("nombre", "nacionalidad")

class LibroAdmin(admin.ModelAdmin):
    list_display = ("titulo","fecha_publicacion","disponible","autor")
    ordering = ("titulo", "autor", "fecha_publicacion")
    search_fields = ("titulo","fecha_publicacion","disponible","autor")
    list_filter = ("titulo", "autor")

admin.site.register(Autor, AutorAdmin)
admin.site.register(Libro, LibroAdmin)