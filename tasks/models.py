from django.db import models

class Task(models.Model):
    ESTATUS_CHOICES = [
        (1, 'Vigente'),
        (0, 'Finalizada'),
    ]

    TAREA_ID = models.AutoField(primary_key=True)
    ESTATUS = models.IntegerField(choices=ESTATUS_CHOICES, default=1)
    TITULO = models.CharField(max_length=50)
    DESCRIPCION = models.CharField(max_length=250, blank=True, null=True)
    FECHA_INICIO = models.DateTimeField(auto_now_add=True)
    FECHA_LIMITE = models.DateTimeField()

    class Meta:
        db_table = 'TAREAS_CARD'

    def __str__(self):
        return self.TITULO
