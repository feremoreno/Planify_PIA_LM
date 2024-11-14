# tasks/forms.py
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['TITULO', 'DESCRIPCION', 'FECHA_LIMITE']
