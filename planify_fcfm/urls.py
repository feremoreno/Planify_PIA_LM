"""
URL configuration for planify_fcfm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
# Planify_PIA/urls.py
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

# Vista para redirigir a la lista de tareas
def home(request):
    return redirect('tasks_list')  # Redirige a la vista de lista de tareas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),  # Ruta para la raíz redirigiendo a tasks_list
    path('tasks/', include('tasks.urls')),  # Incluir las URLs de la app tasks
]
