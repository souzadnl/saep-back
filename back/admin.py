from django.contrib import admin
from .models import Tarefa
from .models import Usuario

admin.site.register(Usuario)
admin.site.register(Tarefa)