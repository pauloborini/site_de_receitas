from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.


class Receita(models.Model):
    pessoa = models.ForeignKey(User, on_delete=models.CASCADE)
    nome_receita = models.CharField(max_length=30)
    ingredientes = models.TextField()
    modo_de_preparo = models.TextField()
    tempo_de_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=30)
    categoria = models.CharField(max_length=30)
    data_receita = models.DateTimeField(default=datetime.now, blank=True)
    publicada = models.BooleanField(default=False)
    foto_receita = models.ImageField(upload_to='fotos/%d/%m/%Y', blank=True)

    def __str__(self):
        return self.nome_receita
