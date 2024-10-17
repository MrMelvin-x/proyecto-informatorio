from django.db import models
from django.utils import timezone
from categorias.models import Categoria

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    categorias = models.ManyToManyField(Categoria)  # Relación de muchas categorías por publicación

    def __str__(self):
        return self.title
# Create your models here.