from django.shortcuts import render,get_object_or_404
from .models import Articulo, Categoria
from django.core.paginator import Paginator #permite paginar los articulos
from django.contrib.auth.decorators import login_required #permite proteger las vistas


# Create your views here.
@login_required(login_url='login') #permite proteger la vista
def articulos(request):

    articulos = Articulo.objects.all()

    paginator = Paginator(articulos, 2)
    page = request.GET.get('page')
    page_articles = paginator.get_page(page)

    return render(request,'articulos/view.html',{
        'title':"TODOS LOS ARTICULOS",
        'articles':page_articles
    })

@login_required(login_url='login') #permite proteger la vista
def category(request, category_id):

    categorias = get_object_or_404(Categoria, id = category_id)
    articulos2 = Articulo.objects.filter(categoria = category_id)

    return render(request,'categorias/categorias.html',{
        'categoria':categorias,
        'articles':articulos2
    })
   
@login_required(login_url='login') #permite proteger la vista
def articulo(request, articulo_id):

    
    articulos = get_object_or_404(Articulo, id = articulo_id)

    return render(request,'articulos/articulo.html',{
        'article':articulos
    })