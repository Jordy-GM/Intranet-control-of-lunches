# Importa la clase ModelForm desde el módulo django.form, ModelForm genera un formulario con campos correspondientes a los atributos de un modelo
#from django.forms import ModelForm
from django import forms
from .models import Task, Menu
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Opciones para el campo "departamento"
DEPARTMENT_CHOICES = [
    ('Almacén', 'Almacén'),
    ('Auditoría', 'Auditoría'),
    ('Calidad y Seguridad', 'Calidad y Seguridad'),
    ('Capacitación', 'Capacitación'),
    ('Comunicación Interna', 'Comunicación Interna'),
    ('Compras', 'Compras'),
    ('Contabilidad', 'Contabilidad'),
    ('Control de Calidad', 'Control de Calidad'),
    ('Diseño', 'Diseño'),
    ('Finanzas', 'Finanzas'),
    ('Gerencia', 'Gerencia'),
    ('Innovación', 'Innovación'),
    ('Inteligencia de Negocios', 'Inteligencia de Negocios'),
    ('Investigación y Desarrollo', 'Investigación y Desarrollo'),
    ('IT', 'IT'),
    ('Legal', 'Legal'),
    ('Logística', 'Logística'),
    ('Mantenimiento', 'Mantenimiento'),
    ('Marketing', 'Marketing'),
    ('Materia Prima', 'Materia Prima'),
    ('Operaciones', 'Operaciones'),
    ('Planificación Estratégica', 'Planificación Estratégica'),
    ('Producción', 'Producción'),
    ('Proyectos', 'Proyectos'),
    ('Recepción', 'Recepción'),
    ('Recursos Humanos', 'Recursos Humanos'),
    ('Relaciones Públicas', 'Relaciones Públicas'),
    ('Seguridad Industrial', 'Seguridad Industrial'),
    ('Servicio al Cliente', 'Servicio al Cliente'),
    ('Soporte Técnico', 'Soporte Técnico'),
    ('Transporte', 'Transporte'),
    ('Ventas', 'Ventas'),
]

class CustomUserCreationForm(UserCreationForm):
    departamento = forms.ChoiceField(choices=DEPARTMENT_CHOICES, label='Departamento', required=True)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'departamento']
        
        



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