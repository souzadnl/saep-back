from django.db import models
from django.utils import timezone

FAZER = 'A Fazer'
FAZENDO = 'Fazendo'
PRONTO = 'Pronto'

class Usuario(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class Tarefa(models.Model):
    description = models.CharField(max_length=200)
    setor = models.CharField(max_length=200)
    priority = models.CharField(max_length=200)
    
    linked = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="tarefas")
    
    STATUS = [
        (FAZER, "A Fazer"),
        (FAZENDO, "Fazendo"),
        (PRONTO, "Pronto"),
    ]

    status = models.CharField(
        max_length=50,
        choices=STATUS,
        default=FAZER,
    )

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.description
