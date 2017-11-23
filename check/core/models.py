from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    pass


class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    celular = models.CharField(max_length=50)
    telefone = models.CharField(max_length=50)
    email = models.EmailField()
    limite_compra = models.FloatField(verbose_name='limite de compra')
    observacao = models.TextField()

    def __str__(self):
        return self.nome


class Fornecedor(models.Model):
    TIPO_PESSOA = (
        (1, 'física'),
        (2, 'jurídica'),
    )
    nome = models.CharField(max_length=50)
    tipo = models.IntegerField(choices=TIPO_PESSOA, verbose_name='Tipo de pessoa')
    cpf_cnpj = models.CharField(max_length=50, verbose_name='CPF/CNPJ')
    ie = models.CharField(max_length=50, verbose_name='inscrição estadual')
    rg = models.CharField(max_length=50, verbose_name='RG')
    telefone = models.CharField(max_length=50)
    fax = models.CharField(max_length=50)
    email = models.EmailField()
    responsavel = models.CharField(max_length=50, verbose_name='responsável')

    def __str__(self):
        return self.nome


class Fornecedor(models.Model):
    TIPO_PESSOA = (
        (1, 'física'),
        (2, 'jurídica'),
    )
    nome = models.CharField(max_length=50)
    tipo = models.IntegerField(choices=TIPO_PESSOA, verbose_name='Tipo de pessoa')
    cpf_cnpj = models.CharField(max_length=50, verbose_name='CPF/CNPJ')
    ie = models.CharField(max_length=50, verbose_name='inscrição estadual')
    rg = models.CharField(max_length=50, verbose_name='RG')
    telefone = models.CharField(max_length=50)
    fax = models.CharField(max_length=50)
    email = models.EmailField()
    responsavel = models.CharField(max_length=50, verbose_name='responsável')

    def __str__(self):
        return self.nome


class Banco(models.Model):
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=50)
    fax = models.CharField(max_length=50)
    agencia = models.IntegerField(verbose_name='agência')
    contato = models.CharField(max_length=50, verbose_name='pessoa de contato')

    def __str__(self):
        return str(self.agencia) + " " + self.nome

class Terceiro(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    negativado = models.BooleanField()
    limite_compra = models.FloatField(verbose_name='limite de compra')
    telefone = models.CharField(max_length=50)
    cpf = models.CharField(max_length=50, verbose_name='CPF')
    rg = models.CharField(max_length=50, verbose_name='RG')

    def __str__(self):
        return self.nome
