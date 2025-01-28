from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from .forms import CreateTaskForm, MenuForm
from .models import Task, Menu, Menuselection
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError 
from django.http import JsonResponse
from collections import defaultdict
from itertools import groupby
from operator import attrgetter



def Home(request):
    return render(request, 'home.html')


def cerrar_sesion(request):

    logout(request)
    return redirect('home')


def iniciar_sesion(request):

    if request.method == 'GET':
        return render(request, 'iniciar_sesion.html', {
            'form': AuthenticationForm()
        })

    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])

        if user is None:
            return render(request, 'iniciar_sesion.html', {
                'form': AuthenticationForm(),
                'error': 'user o password incorrecto'
            })

        else:
            login(request, user)
            return redirect('tasks')


def create_tasks(requests):

    if requests.method == 'GET':
        return render(requests, 'create_tasks.html', {
            'form': CreateTaskForm
        })
    else:
        if requests.method == 'POST':
            try:
                # print(requests.POST)

                # transforma los datos recibidos por Querydict, en formularios html y los almacena en la variable form
                form = CreateTaskForm(requests.POST)
                # Crea una nueva instancia del modelo a partir del formulario, pero no la guarda aún en la base de datos (commit=False)
                nuevatarea = form.save(commit=False)
                # Asigna el usuario actual (quien hizo la solicitud) como el propietario de la nueva tarea
                nuevatarea.user = requests.user
                # Guarda la nueva tarea en la base de datos, ahora con todos los campos completados
                nuevatarea.save()
                # Redirige al usuario a la vista de tareas una vez que la nueva tarea ha sido guardada con éxito
                return redirect('tasks')
            except:
                ValueError
            return render(requests, 'create_tasks.html', {
                'form': CreateTaskForm,
                'error': 'no se pudo guardar los datos o los datos no son validos'


            })


def Signup(request):
    if request.method == 'GET':
        # Si el método de la solicitud es GET, renderiza la página 'signup.html'
        # y pasa el formulario 'UserCreationForm' como contexto a la plantilla.
        return render(request, 'signup.html', {
            'form': UserCreationForm()
        })
    else:
        # Si el método de la solicitud es POST, comprueba que las contraseñas
        # ingresadas en 'password1' y 'password2' coincidan.
        if request.POST['password1'] == request.POST['password2']:
            try:
                # Si las contraseñas coinciden, intenta crear un nuevo usuario
                # utilizando el nombre de usuario y la contraseña proporcionados.
                user = User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password1']
                )
                # Guarda el nuevo usuario en la base de datos.
                user.save()
                # Esta línea autentica al usuario y establece la sesión de usuario, establece una cookie en el navegador del usuario que mantiene su sesión activa.
                login(request, user)
                # Devuelve una respuesta indicando que el usuario se creó con éxito.
                return redirect('tasks')
                # return HttpResponse('User created successfully')

            except:
                # Si ocurre algún error, como que el nombre de usuario ya exista,
                # devuelve una respuesta indicando que el nombre de usuario ya existe en la mima pagina con el formulario
                return render(request, 'signup.html', {
                    'form': UserCreationForm(),
                    "error": 'uuario ya existe'})

        # Si las contraseñas no coinciden, devuelve una respuesta indicando que no coinciden. con la mima pagina formulario
        return render(request, 'signup.html', {
            'form': UserCreationForm(),
            "error": 'la contraeña no eite'})


def tasks(request):
    # devuelve todas las tareas creadas de la base de datos de todos los usuarios
    # tasks = Task.objects.all()

    # Obtiene solo las tareas del usuario actualmente logueado
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'tasks.html', {
        'tasks': tasks
    })


def tasks_completed(request):
    if request.user.is_authenticated:

        tasks = Task.objects.filter(user=request.user, datecompleted__isnull=False).order_by(
            'datecompleted')     # Obtiene solo las tareas del usuario actualmente logueado
        return render(request, 'tasks.html', {
            'tasks': tasks
        })
    else:
        return render(request, 'home.html', {'error': 'Debes iniciar sesión para acceder a esta página.'})


# la función recibe una solicitud (request) y un número de identificación (id).
def task_detail(request, id):
    if request.method == 'GET':
        # busca una tarea en la base de datos que tenga el mismo número de identificación (id) que se le pasó a la función. pk, se usa get_object_or_404 para evitar errores
        task = get_object_or_404(Task, pk=id, user=request.user)
        # llena el formulario obtenidos de la DB y los llena en el formulario CreateTaskForm y lo almacena en variable form par apasarla al html
        form = CreateTaskForm(instance=task)
        return render(request, 'task_detail.html', {  # Renderiza la plantilla 'task_detail.html' y pasa el objeto 'task' al contexto de la plantilla. pasa el objeto form a la plantilla html front
            'task': task,
            'form': form
        })
    else:
        try:  # en caso que exista un error
            # dame solo las tareas del usuario que estoy logeado y almacena en variable task
            task = get_object_or_404(Task,  pk=id, user=request.user)
            # carga los datos del POST en el formulario osea los datos que te voy a escribir (enviar)
            form = CreateTaskForm(request.POST, instance=task)
            form.save()  # guarda o catualiza los datos que te estoy enviando por metodo POST en DB
            return redirect('tasks')  # Renderiza la plantilla task

        except ValueError:  # en caso que exista un error
            return render(request, 'task_detail.html', {  # Renderiza la plantilla 'task_detail.html' y pasa el objeto 'task' al contexto de la plantilla. pasa el objeto form a la plantilla html front
                'task': task,
                'form': form,
                'error': 'no se pudo actualizar la tarea requerida'
            })


def delete_task(request, id):  # elimina una tarea en la bae de dato
    # obten la tarea de la DB  que tenga el mismo id que se le paso a la funcion y que pertenezca al usuario
    task = get_object_or_404(Task, pk=id, user=request.user)
    if request.method == 'POST':  # i te envio una peticion pot por elimina la tarea
        task.delete()
        return redirect('tasks')


def complete_task(request, id):
    # obten la tarea de la DB  que tenga el mismo id que se le paso a la funcion y que pertenezca al usuario
    task = get_object_or_404(Task, pk=id, user=request.user)
    if request.method == 'POST':  # Si la solicitud es de tipo POST
        task.datecompleted = timezone.now()  # Asigna la fecha y hora actual a la tarea
        task.save()  # Guarda los cambios en la base de datos
        return redirect('tasks')  # Redirige a la vista de la lista de tareas


# 01:53:04 Actualizar tarea


######################## menu de alimento ##################################################################################################

# Vista para que el administrador suba los menús




@login_required  # Este decorador asegura que solo los usuarios autenticados puedan acceder a esta vista.
def upload_menu(request):
    # Verifica si el usuario es un superusuario o tiene el nombre de usuario 'yandry'.
    if request.user.is_superuser or request.user.username == 'yandry': 
        
        # Si la solicitud es de tipo POST, se procesa el formulario enviado.
        if request.method == 'POST':  

            form_prefix = None   
            # Itera del 1 al 5 para identificar qué formulario fue enviado.
            for i in range(1, 6): 
                if f'form{i}-day' in request.POST:
                    form_prefix = f'form{i}'  # Asigna el prefijo del formulario encontrado.
                    break

            # Si se encontró un prefijo de formulario válido, se procesa el formulario.
            if form_prefix:
                form = MenuForm(request.POST, prefix=form_prefix)
                if form.is_valid():  # Valida el formulario.
                    form.save()  # Guarda los datos del formulario en la base de datos.
                    return JsonResponse({'status': 'success'})  # Retorna una respuesta JSON de éxito.
                else:
                    return JsonResponse({'status': 'error', 'errors': form.errors})  # Retorna errores si el formulario no es válido.

        # Si la solicitud no es POST, se inicializan 5 formularios con prefijos únicos.
        forms = {f'form{i}': MenuForm(prefix=f'form{i}') for i in range(1, 6)}
        
        # Lista de días de la semana para usar en la plantilla.
        days_of_week = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']
        
        # Obtiene las selecciones de menú de la base de datos, agrupadas por usuario.
        seleccion = Menuselection.objects.select_related('user', 'menu').order_by('user__username', 'menu__day')
        grouped_data = {}
        # Agrupa las selecciones por nombre de usuario.
        for user, items in groupby(seleccion, key=attrgetter('user.username')):
            grouped_data[user] = list(items)
        
        # Renderiza la plantilla 'upload_menu.html' con los datos agrupados, los formularios y los días de la semana.
        return render(request, 'upload_menu.html', {'seleccion': grouped_data, 'forms':forms, 'days_of_week': days_of_week} )
    

    else:
        # Si el usuario no tiene permisos, se redirige a la página de inicio con un mensaje de error.
        return render(request, 'home.html', {'error': 'No tienes permisos para acceder a esta página.'})
    
    



def seleccionados(request):
    if request.user.is_superuser or request.user.username == 'yandry':
        seleccion = Menuselection.objects.select_related('user', 'menu').order_by('user__username', 'menu__day')
        grouped_data = groupby(seleccion, key=attrgetter('user.username'))

        return render(request, 'upload_menu.html', {'seleccion': grouped_data})
    else:
        return render(request, 'home.html', {'error': 'No tienes permisos para acceder a esta página.'})


# la función recibe una solicitud (request) y un número de identificación (id).
def detalle_menu(request, menu_id):

    if request.user.is_superuser or request.user.username == 'yandry':

        menu = get_object_or_404(Menu, id=menu_id)

        if request.method == 'GET':
            # llena el formulario obtenidos de la DB y los llena en el formulario CreateTaskForm y lo almacena en variable form par apasarla al html
            form = MenuForm(instance=menu)
            return render(request, 'detalle_menu.html', {  # Renderiza la plantilla 'task_detail.html' y pasa el objeto 'task' al contexto de la plantilla. pasa el objeto form a la plantilla html front
                'menu': menu,
                'form': form
            })
        else:
            try:  # en caso que exista un error
                # menu = get_object_or_404(Menu, id=menu_id) # dame solo las tareas del usuario que estoy logeado y almacena en variable task
                # carga los datos del POST en el formulario osea los datos que te voy a escribir (enviar)
                form = MenuForm(request.POST, instance=menu)
                if form.is_valid():
                    form.save()  # guarda o catualiza los datos que te estoy enviando por metodo POST en DB
                    return redirect('menu_list')  # Renderiza la plantilla

            except ValueError:  # en caso que exista un error
                return render(request, 'detalle_menu.html', {  # Renderiza la plantilla 'task_detail.html' y pasa el objeto 'task' al contexto de la plantilla. pasa el objeto form a la plantilla html front
                    'menu': menu,
                    'form': form,
                    'error': 'no se pudo actualizar el menu'
                })
    else:
        return render(request, 'home.html', {'error': 'Debes tener los permisos necesarios para acceder a esta página.'})


def eliminar_menu(request, menu_id):
    if request.user.is_superuser or request.user.username == 'yandry':
        # Busca un objeto del modelo 'Menu' cuyo 'id' coincida con el valor de 'menu_id'.
        menu = get_object_or_404(Menu, id=menu_id)
        if request.POST:
            menu.delete()  # Elimina el objeto menu de la base de datos
            return redirect('menu_list')
    else:
        return render(request, 'home.html', {'error': 'Debes tener los permisos necesarios para acceder a esta página.'})

# Vista para que los usuarios seleccionen un menú


@login_required  # decorador que restringue vistas a usuarios no authenticados
def menu_list(request):
    
    menus = Menu.objects.all()   # Obtiene todos los objetos del modelo 'Menu'
    if request.method == 'POST':   # si el metodo es POST
        selected_menu_ids = request.POST.getlist('menu')   # Obtiene la lista de IDs de los menús seleccionados
        for menu_id in selected_menu_ids:    # recorre la lista de IDs de los menús seleccionados
            selected_menu = get_object_or_404(Menu, id=menu_id)   # Obtiene el objeto del modelo 'Menu' cuyo 'id' coincida con el valor de 'menu_id' o devuelve un error 404 si no se encuentra
            if not Menuselection.objects.filter(user=request.user, menu=selected_menu).exists():    # Verifica si el usuario actual ya seleccionó el menú
                Menuselection.objects.create(user=request.user, menu=selected_menu) # Crea un nuevo registro en el modelo 'Menuselection' asignando el usuario actual y el menú seleccionado
        return redirect('menu_list') #redirecciona a la lista de menu

    return render(request, 'menu_list.html', {'menus': menus})   # Renderiza la plantilla 'menu_list.html' y pasa la lista de menús a

