from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from . import models, forms


# Create your views here.

@login_required
def home(request):
    """
    Vista que representa la interacción con el home
    """
    
    #Crear form
    form_events=forms.EventForm()

    #Comprobar que los eventos se guarden en el usuario correspondiente 
    user_events= models.Events.objects.filter(user=request.user)

    form_goals=forms.GoalsForm()

    user_goals= models.Goals.objects.filter(user=request.user)


    return render(request, "tma/home/home.html", {"form_events": form_events, "events": user_events, "form_goals": form_goals, "goals": user_goals})


@login_required   
def add_events(request):
    """
    Vista que representa la creación de un nuevo evento
    """

    if request.method == 'POST':
        #Crear el formulario para el evento
        form=forms.EventForm(request.POST)

        if form.is_valid():

            #Guardar el formulario
            event=form.save(commit=False)

            #Asociar el evento al usuario de la sesión
            event.user=request.user

            #Guardar todo junto
            event.save()

            #Redirigir al home actualizado
            return redirect('home')
    
    return redirect('home')


@login_required
def delete_event(request, event_id):
    """
    Vista que representa la eliminación de un evento
    """

    #Buscar el evento con el id asociado en la sesión actual
    event=get_object_or_404(models.Events, id=event_id, user=request.user)
    
    if request.method == "POST":

        #Eliminar ese evento
        event.delete()

        return redirect('home')
    
    return redirect('home')

"""
GOALS
"""

@login_required   
def add_goals(request):
    """
    Vista que representa la creación de un nuevo goal
    """

    if request.method == 'POST':
        #Crear el formulario para el evento
        form=forms.GoalsForm(request.POST)

        if form.is_valid():

            #Guardar el formulario
            event=form.save(commit=False)

            #Asociar el evento al usuario de la sesión
            event.user=request.user

            #Guardar todo junto
            event.save()

            #Redirigir al home actualizado
            return redirect('home')
    
    return redirect('home')

@login_required
def delete_goal(request, goal_id):
    """
    Vista que representa la eliminación de un evento
    """

    #Buscar el evento con el id asociado en la sesión actual
    goal=get_object_or_404(models.Goals, id=goal_id, user=request.user)
    
    if request.method == "POST":

        #Eliminar ese evento
        goal.delete()

        return redirect('home')
    
    return redirect('home')














@login_required
def atp(request):
    return render(request, "tma/atp/atp.html")

