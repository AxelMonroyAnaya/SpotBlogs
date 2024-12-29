from django.shortcuts import render,redirect
from django.contrib import messages #permite enviar mensajes flash
from django.contrib.auth.forms import UserCreationForm
from .forms import Form_Registro
from django.contrib.auth import authenticate, login, logout #permite autenticar, iniciar sesion y cerrar sesion
from django.contrib.auth.decorators import login_required #permite proteger las vistas

# Create your views here.

def index(request):
    return render(request,"mainapp/index.html",{
        'title':'inicio'
    })

def about(request):
    return render(request, "mainapp/sobre_Us.html",{
        'title':'sobre nosotros'
    })

def registro(request):

    if request.user.is_authenticated:
        return redirect('index')
    else:
        registro_form = Form_Registro()

        if request.method == 'POST':
            registro_form = Form_Registro(request.POST)
            if registro_form.is_valid():
                registro_form.save()
                messages.success(request, 'Registro exitoso')
                return redirect('index')

        return render(request, "usuarios/registro.html",{
            'title':'Registro',
            'registro_form':registro_form
        })

def sesion(request):
    
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            usuario = authenticate(request, username=username, password=password)
            if usuario is not None:
                login(request, usuario)
                messages.success(request, 'Bienvenido {}'.format(usuario.username))
                return redirect('index')
            else:
                messages.error(request, 'Credenciales incorrectas')
                return redirect('login')

        return render(request, "usuarios/login.html",{
            'title':'Iniciar sesion'
        })

def cerrar_sesion(request):
    logout(request)
    messages.success(request, 'Sesion cerrada')
    return redirect('login')