from django.shortcuts import get_object_or_404, redirect, render
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, PostView, Like, Comment
from .forms import CommentForm, PostForm
from .models import Libro, Resena
from .forms import ResenaForm

def libro_detalle(request, libro_id):
    libro = Libro.objects.get(pk=libro_id)
    reseñas = Resena.objects.filter(libro=libro)
    return render(request, 'libro_detalle.html', {'libro': libro, 'reseñas': reseñas})


def libro_detalle(request, libro_id):
    libro = Libro.objects.get(pk=libro_id)
    reseñas = Resena.objects.filter(libro=libro)
    return render(request, 'libro_detalle.html', {'libro': libro, 'reseñas': reseñas})

def agregar_resena(request, libro_id):
    libro = Libro.objects.get(pk=libro_id)
    if request.method == 'POST':
        form = ResenaForm(request.POST)
        if form.is_valid():
            resena = form.save(commit=False)
            resena.usuario = request.user
            resena.libro = libro
            resena.save()
            return redirect('libro_detalle', libro_id=libro_id)
    else:
        form = ResenaForm()
    return render(request, 'agregar_resena.html', {'form': form, 'libro': libro})

# Create your views here.

# Importamos las vistas genericas y creamos nuevas vist e importamos ls modelos.
class PostListView(ListView):
    model = Post
    
class PostDetailView(DetailView):
    model = Post
    
    def post (self, *args, **kwargs):
        form = CommentForm(self.request.POST)
        if form.is_valid():
            post = self.get_object()
            comment = form.instance
            comment.user = self.request.user
            comment.post = post
            comment.save()
            return redirect('detail', slug=post.slug)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'form': CommentForm()
            
        })
        return context
    
    def get_object(self, **kwargs):
        object = super().get_object(**kwargs)
        if self.request.user.is_authenticated:
              PostView.objects.get_or_create(user=self.request.user, post=object)
        return object 
    
    
class PostCreateView(CreateView):
    form_class = PostForm
    model = Post
    success_url = '/' 
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type':'create'
        })
        return context

class PostUpdateView(UpdateView):
     form_class = PostForm
     model = Post
     success_url = '/' 
     def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type':'update'
        })
        return context 
    
class PostDeleteView(DeleteView):
    model = Post
    
    success_url = '/'
    
def like(request, slug):
    post= get_object_or_404(Post, slug = slug)
    like_qs = Like.objects.filter(user=request.user, post=post)
    if like_qs.exists():
        like_qs[0].delete()
        return redirect('detail', slug=slug)
    Like.objects.create(user=request.user, post=post)
    return redirect('detail', slug=slug)
    



