from django.shortcuts import render
from .models import Page
from django.contrib.auth.decorators import login_required #permite proteger las vistas

# Create your views here.
@login_required(login_url='login') #permite proteger la vista
def page(request, slug):

    page = Page.objects.get(slug = slug)


    return render(request, 'pages/page.html',{
        'title':page.title,
        'page':page
    })