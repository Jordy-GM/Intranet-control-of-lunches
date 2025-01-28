# Importa la clase ModelForm desde el módulo django.form, ModelForm genera un formulario con campos correspondientes a los atributos de un modelo
#from django.forms import ModelForm
from django import forms
from .models import Task, Menu


class CreateTaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'description', 'important']
        
        


######################## menu de alimento ##################################################################################################

class MenuForm(forms.ModelForm):
    form_type = forms.CharField(widget=forms.HiddenInput())  # Campo oculto

    class Meta:
        model = Menu
        fields = ['day', 'option_number', 'soup', 'rice', 'protein', 'guarnicion', 'salad', 'drink', 'dessert']
        widgets = {
            'day': forms.DateInput(attrs={'type': 'date'}),  # Para que aparezca el calendario
            
            'option_number': forms.NumberInput(attrs={'min': 1, 'max': 10}),  # Ejemplo para option_number
            'soup': forms.TextInput(attrs={'placeholder': 'Tipo de sopa'}),  # Ejemplo para un campo de texto
            'drink': forms.Select(choices=[('agua', 'Agua'), ('jugo', 'Jugo'), ('gaseosa', 'Gaseosa')]),  # Dropdown para bebida
            # Puedes añadir más widgets según necesites
        } 
    
    def __init__(self, *args, **kwargs):
        super(MenuForm, self).__init__(*args, **kwargs)
        # Puedes personalizar el valor inicial del campo oculto aquí si lo necesitas
        self.fields['form_type'].initial = 'form1'  # Cambia 'form1' según lo necesites