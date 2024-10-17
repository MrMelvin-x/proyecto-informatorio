from django.contrib import admin
from .models import Categoria

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre']  # Mostramos el campo 'nombre' en la lista de categorías
    search_fields = ['nombre']  # Añadimos una barra de búsqueda por nombre

