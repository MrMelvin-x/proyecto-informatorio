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

def categorias(request):
    return render(request, 'blog/categorias.html')

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

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})

def listar_posts(request):
    posts = Post.objects.all()  # Obtén todos los posts
    categorias = Categoria.objects.all()  # Obtén todas las categorías
    ultimosposts = Post.objects.all().order_by('fecha_publicacion')  # Posts ordenados por fecha de publicación


    # Filtrar posts si hay un parámetro de categoría en la URL
    categoria_id = request.GET.get('categoria')
    if categoria_id:
        posts = posts.filter(categorias__id=categoria_id)  # Filtrar posts por categoría

    return render(request, 'categorias.html', {
        'ultimosposts': ultimosposts, 
        'categorias': categorias,
        'mostrar_categorias': True,
        'mostrar_fechas': True,
    })

def listar_categorias(request):
    categorias = Categoria.objects.all()  # Obtén todas las categorías
    posts = Post.objects.all()  # También obtén todos los posts
    return render(request, 'categorias.html', {
        'categorias': categorias,
        'posts': posts,
        'mostrar_cargas': True,
        'mostrar_fechas': True
    })

def listar_posts_por_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)  # Obtener la categoría por ID o dar error 404
    posts = Post.objects.filter(categorias=categoria)  # Filtra posts por categoría seleccionada
    categorias = Categoria.objects.all()  # Obtener todas las categorías

    return render(request, 'filtrado_categorias.html', {
        'posts': posts,
        'categorias': categorias,
        'mostrar_categorias': True,
        'mostrar_fechas': True,
        'mostrar_cargas': True
    })