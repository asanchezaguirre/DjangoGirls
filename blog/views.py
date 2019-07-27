from django.shortcuts import render
from .models import *

# Create your views here.
def Inicio(request, iduser=None):
    if iduser is None:
        p=Post.objects.all()
    else: 
        p=Post.objects.filter(author__id = iduser)
    return render(request, 'blog/home.html', { "publicaciones":p})
