from django.shortcuts import render

# Create your views here.
# tasks/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from django.utils import timezone

# Crear una nueva tarea
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/create_task.html', {'form': form})

# Lista de tareas vigentes
def tasks_list(request):
    tasks = Task.objects.filter(ESTATUS=1)
    return render(request, 'tasks/tasks_list.html', {'tasks': tasks})

# Actualizar tarea
def update_task(request, pk):
    task = get_object_or_404(Task, TAREA_ID=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/update_task.html', {'form': form})

# Eliminar tarea
def delete_task(request, pk):
    task = get_object_or_404(Task, TAREA_ID=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks_list')
    return render(request, 'tasks/delete_task.html', {'task': task})
