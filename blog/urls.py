from django.urls import path
from . import views
from .views import post_list, post_detail

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('cat/', views.categorias, name='categorias'),
    path('about/', views.about, name='about'),
    path('contacto/', views.contacto, name='contacto'),
    path('post/new/', views.create_post, name='create-post'),  
    path('post/<int:post_id>/', post_detail, name='post_detail'),
]