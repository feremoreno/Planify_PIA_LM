from django.db import models

# Create your models here.
from django.db import models

class Task(models.Model):
    TAREA_ID = models.AutoField(primary_key=True)
    ESTATUS = models.IntegerField(default=1)  # 1: vigente, 0: finalizada
    TITULO = models.CharField(max_length=50)
    DESCRIPCION = models.CharField(max_length=250, blank=True, null=True)
    FECHA_INICIO = models.DateTimeField(auto_now_add=True)
    FECHA_LIMITE = models.DateTimeField()

    def __str__(self):
        return self.TITULO
