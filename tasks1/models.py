from django.db import models
from django.contrib.auth.models import User


# modelo de signup 

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username + ' | ' + self.department



##############tareas@#####################
class Task(models.Model):

    title = models.CharField(max_length=100)  # Campo de texto para el título de la tarea. Es obligatorio y tiene un máximo de 100 caracteres.
    
    description = models.TextField(blank=True)  # Campo de texto para la descripción de la tarea. Es opcional ('blank=True').
   
    created = models.DateTimeField(auto_now_add=True)  # Campo de fecha y hora que se establece automáticamente al crear la tarea.
    
    datecompleted = models.DateTimeField(null=True, blank=True)  # Campo de fecha y hora que indica cuándo se completó la tarea. Puede ser nulo ('null=True') y blank=true solo es opcional para el admin
   
    important = models.BooleanField(default=False)  # Campo booleano que indica si la tarea es importante. Valor por defecto es False.
   
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Relación de clave foránea con el modelo User, para identificar al usuario que creó la tarea.

    
    def __str__(self):
        return self.title + ' | por el usuario | ' + self.user.username + ' |'



######################## menu de alimento ##################################################################################################

class Menu(models.Model):
    day = models.DateField()
    option_number = models.IntegerField()
    soup = models.CharField(max_length=100)
    rice = models.CharField(max_length=100)
    protein = models.CharField(max_length=100)
    guarnicion = models.CharField(max_length=100)
    salad = models.CharField(max_length=100)
    drink = models.CharField(max_length=100)
    dessert = models.CharField(max_length=100)
    
    #campp ia m
    name = models.CharField(max_length=255, default="Sin nombre")
    description = models.TextField(blank=True)
    calories = models.IntegerField(default=0)
    fats = models.IntegerField(default=0)
    carbohydrates = models.IntegerField(default=0)
    gluten_free = models.BooleanField(default=False)
    vegan = models.BooleanField(default=False)
    low_carb = models.BooleanField(default=False)

    def __str__(self):
        return f'Menu {self.option_number} para el dia {self.day}'

class Menuselection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_selections')
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='menu_selections')
    date_selected = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} selecciono {self.menu} el {self.date_selected}' 
    
    
    
    
    