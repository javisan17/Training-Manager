from django import forms
from .models import Events

class EventForm(forms.ModelForm):

    type_choices= [
        ('RUN', 'Running'),
        ('BIK', 'Ciclismo'),
        ('SWM', 'Natación'),
        ('TRI', 'Triatlon'),
        ('GYM', 'Gimnasio')
    ]
    name=forms.CharField(label='Nombre', max_length=30, required=True)
    date=forms.DateField(label='Fecha', required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    type=forms.ChoiceField(label='Tipo de evento', choices=type_choices, required=True)
    description=forms.CharField(label='Descripción', max_length=255)

    class Meta:
        model = Events
        fields = ['name', 'date', 'type', 'description']