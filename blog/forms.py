from django import forms
from .models import Post
from categorias.models import Categoria
        
class PostForm(forms.ModelForm):
    categorias = forms.ModelMultipleChoiceField(
        queryset=Categoria.objects.all(),
        widget=forms.CheckboxSelectMultiple,  
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'created_at', 'categorias']