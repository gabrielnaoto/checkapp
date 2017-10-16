from django.db import models

# Create your models here.

class Cliente(models.Model):
    codigo = models.IntegerField(u'Código')
    nome = models.CharField(u'Nome', max_length=255)
    data_cadastro = models.DateTimeField(u'Data de cadastro')

    def __str__(self):
        return self.nome 
