from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class Categoria(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    description = models.CharField(verbose_name=("descripcion"), max_length=300)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='creado en :')

    def __str__(self):
        return self.name

class Articulo(models.Model):
    title = models.CharField(max_length=30)
    content = RichTextField()
    image = models.ImageField(upload_to='articles', blank=True, null=True)
    user = models.ForeignKey(User,editable=False , on_delete=models.CASCADE)
    categoria = models.ManyToManyField(Categoria, verbose_name='categorias', blank=True)
    public = models.BooleanField(verbose_name="publicado?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='creado en :')

    def __str__(self):
        return self.title

# Create your models here.
