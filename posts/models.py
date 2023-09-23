from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse


# Creando modelo de nuestro user.
# Importamos el usuario base para ser heredado de user.
class User(AbstractUser):
    pass

    def _str_(self):
      return self.username

# Creando modelo post
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    thumbnail = models.ImageField()
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now= True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField()
    
    def _str_(self):
        return self.title
    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.slug})
    
    def get_like_url(self):
        return reverse("like", kwargs={'slug': self.slug})
     
    @property
    def comments(self):
        return self.comment_set.all()
    
    @property
    def get_comment_count(self):
       return self.comment_set.all().count()
   
    @property
    def get_view_count(self):
       return self.postview_set.all().count()
   
    @property
    def get_like_count(self):
       return self.like_set.all().count()
   
# Creando modelo para comentarios.
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE )
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    
    def _str_(self):
        return self.user.username
    
# Creando modelo para vista post.
class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE )
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def _str_(self):
        return self.user.username
    
    
# Creando modelo para likes en las publicaciones.
class Like(models.Model):
    user =models.ForeignKey(User, on_delete=models.CASCADE )
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    def _str_(self):
        return self.user.username
    
class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    descripcion = models.TextField()

class Resena(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='reseñas')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    calificacion = models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])
    comentario = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    