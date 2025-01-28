"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tasks1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Signup/', views.Signup, name='signup'),  # Nombre de la vista corregido a 'signup'
    path('', views.Home, name='home'),  # Nombre de la vista corregido a 'home'
    path('tasks/', views.tasks, name='tasks'),
    path('tasks_completed/', views.tasks_completed, name='tasks_completed'), 
    path('logout/', views.cerrar_sesion, name='logout'),  # Corregido 'cerrar_sesion' como nombre de la vista y ruta sin '/logout'
    path('Signin/', views.iniciar_sesion, name='iniciar_sesion'),
    path('create_tasks/', views.create_tasks, name='create_tasks'),
    path('tasks/<int:id>/', views.task_detail, name='task_detail'),
    path('tasks/<int:id>/delete_task', views.delete_task, name='delete_task'), 
    path('tasks/<int:id>/complete_task', views.complete_task, name='complete_task'), 
    
    ######################## menu de alimento ##################################################################################################

    
    path('upload_menu/', views.upload_menu, name='upload_menu'),
    #path('upload_menu/', views.Seleccionados, name='upload_menu'),
    path('menu_list/', views.menu_list, name='menu_list'),
    
    path('menu_list/<int:menu_id>/', views.detalle_menu, name='detalle_menu'),
    path('menu_list/<int:menu_id>/eliminar_menu', views.eliminar_menu, name='eliminar_menu'), 
    
    
    
    
]





