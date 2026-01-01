from django.db import models
from django.contrib.auth.models import User

class Noticia(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=120)
    contenido = models.TextField()
    creado = models.DateTimeField(auto_now_add=True)

class Recuerdo(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=120)
    descripcion = models.TextField(blank=True)
    archivo = models.FileField(upload_to='recuerdos/')
    creado = models.DateTimeField(auto_now_add=True)

class ItemResenable(models.Model):
    nombre = models.CharField(max_length=120)
    categoria = models.CharField(max_length=50)
    creado = models.DateTimeField(auto_now_add=True)

class Resena(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(ItemResenable, on_delete=models.CASCADE)
    puntaje = models.PositiveSmallIntegerField()
    comentario = models.TextField()
    creado = models.DateTimeField(auto_now_add=True)
