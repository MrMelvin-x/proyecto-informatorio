from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
from categorias.models import Categoria

def inicio(request):
    posts = Post.objects.all().order_by('-created_at')  # Ordenamos por fecha de creación, más recientes primero
    return render(request,"blog/inicio.html", {'posts': posts})

def about(request):
    return render(request, 'blog/about.html')

#def categorias(request):
#    return render(request, 'blog/categorias.html')

def contacto(request):
    return render(request, 'blog/contacto.html')

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo post en la base de datos
            return redirect('inicio')  # Redirige a la página de inicio después de guardar
    else:
        form = PostForm()

    return render(request, 'blog/create_post.html', {'form': form})



