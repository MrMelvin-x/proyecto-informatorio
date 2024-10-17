from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('about/', views.about, name='about'),
    path('contacto/', views.contacto, name='contacto'),
    path('post/new/', views.create_post, name='create-post'),  # URL para crear nuevas publicaciones
]