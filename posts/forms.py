from django import forms
from .models import Post, Comment
from .models import Resena

class ResenaForm(forms.ModelForm):
    class Meta:
        model = Resena
        fields = ['calificacion', 'comentario']

class PostForm( forms.ModelForm):
    class Meta:
        model = Post
        fields = ('__all__')
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)