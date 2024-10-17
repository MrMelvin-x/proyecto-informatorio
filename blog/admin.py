from django.contrib import admin
from .models import Post
from categorias.models import Categoria

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['categorias', 'created_at']  # Filtrar publicaciones por categoría y fecha
    search_fields = ['title', 'content']
    filter_horizontal = ('categorias',)  # Para mostrar las categorías como un selector horizontal

    # Opcional: para mostrar más detalles del post
    fieldsets = (
        (None, {
            'fields': ('title', 'content', 'categorias')
        }),
        ('Dates', {
            'fields': ('created_at',)
        }),
    )