from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


# Create your views here.

class VRegister(View):
    """
    Registrar los usuarios
    """

    def get(self, request):
        """
        GET: mostrar la información de la página correspondiente
        """

        #Crear un formulario de resgitro con la clase UserCreationForm
        form=UserCreationForm()

        #Renderizaz y mostrar
        return render(request, "authentication/register/register.html", {"form": form})
    
    def post(self, request):
        """
        POST: gestionar que se hace después de dar al form
        """

        #Rellenar el formulario de registro de la clase UserCreationForm con la información del POST
        form=UserCreationForm(data=request.POST)

        if form.is_valid():

            #Almacenar el usuario en la db
            usuario=form.save()

            #Iniciar sesión nada más registrarse
            login(request, usuario)

            #Redireccionar al inicio (home)
            return redirect('home')
        
        else:

            for msg in form.error_messages:

                #Crear los errores cometidos y mostrarlos por la clase UserCreationForm
                messages.error(request, form.error_messages[msg])

            #Mostrar el mismo formulario para que se reintente
            return render(request, "authentication/register/register.html", {"form": form})

def my_logout(request):
    """
    Cerrar sesión
    """

    #Cerrar sesión del usuario
    logout(request)

    #Redirecionar al home
    return redirect('home')



class VLogin(View):
    """
    Iniciar sesión de usuarios
    """
    
    def get(self, request):
        """
        GET: mostrar la información de la página correspondiente
        """

        #Crear un formulario de login con la clase AuthenticationForm
        form=AuthenticationForm()

        #Renderizaz y mostrar
        return render(request, "authentication/login/login.html", {"form": form})
    
    def post(self, request):
        """
        POST: gestionar que se hace después de dar al form
        """

        #Rellenar el formulario de registro de la clase UserCreationForm con la información del POST
        form=AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            #Capturar la informacion de ambos cuadros de texto
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')

            #Autentificar la información en la db
            user=authenticate(username=username, password=password)

            #Si existe el usuario
            if user is not None:

                #Logearse
                login(request, user)

                #Redireccionar a home
                return redirect('home')
            
            else:

                #Crear los errores cometidos. Estos se deben mostrar por el html
                messages.error(request, "Usuario no válido")

        else:

            #Crear los errores cometidos. Estos se deben mostrar por el html
            messages.error(request, 'Información incorrecta')

        #Crear un formulario de login con la clase AuthenticationForm
        form=AuthenticationForm()

        #Renderizaz y mostrar
        return render(request, "authentication/login/login.html", {"form": form})