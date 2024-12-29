from blog.models import Categoria,Articulo

def get_Categorias(request):
    
    #subconsulta
    ids = Articulo.objects.filter(public = True).values_list( 'categoria', flat=True)
    Categoria1 = Categoria.objects.filter(id__in =  ids).values_list('id', 'name')

    return{
        'categorias':Categoria1,
        'public': ids
    }