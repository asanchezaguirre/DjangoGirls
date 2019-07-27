from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User

# Create your views here.
def Inicio(request, iduser=None):
    if iduser is None:
        p=Post.objects.all()
    else: 
        p=Post.objects.filter(author__id = iduser)
    return render(request, 'blog/home.html', { "publicaciones":p})

def Publicar(request):
    if request.method=="GET":
        u=User.objects.filter(is_active = True)
        return render(request, 'blog/publicar.html', { "usuario":u })
    elif request.method=="POST":
        us=User.objects.get(id=request.POST.get('user'))
        p=Post()
        p.author=us
        p.title=request.POST.get('title')
        p.text=request.POST.get('text')
        p.save()
        u=User.objects.filter(is_active = True)
        return render(request, 'blog/publicar.html', { "usuario":u, "publicacion":p })

