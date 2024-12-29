from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField()
    order = models.IntegerField(default=0, verbose_name="orden")
    slug = models.CharField(unique=True,max_length=100)
    public = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'pagina'
        verbose_name_plural = 'Paginas'

    def __str__(self):
        return self.title