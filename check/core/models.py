from _ast import For

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class Empresa(models.Model):
    nome = models.CharField(max_length=50)
    cnpj = models.CharField(max_length=50, verbose_name='CPF/CNPJ')
    ie = models.CharField(max_length=50, verbose_name='inscrição estadual', blank=True, null=True)
    logradouro = models.CharField(max_length=50)
    numero = models.IntegerField()
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    uf = models.CharField(max_length=2, verbose_name='UF')
    cep = models.CharField(max_length=50, verbose_name='CEP')
    # contato
    telefone = models.CharField(max_length=50)
    fax = models.CharField(max_length=50)


class User(AbstractUser):
    empresa = models.ForeignKey(Empresa)


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
        (1, 'Física'),
        (2, 'Jurídica'),
    )
    nome = models.CharField(max_length=50)
    tipo = models.IntegerField(choices=TIPO_PESSOA, verbose_name='Tipo de pessoa')
    cpf_cnpj = models.CharField(max_length=50, verbose_name='CPF/CNPJ')
    ie = models.CharField(max_length=50, verbose_name='inscrição estadual', blank=True, null=True)
    rg = models.CharField(max_length=50, verbose_name='RG', blank=True, null=True)
    responsavel = models.CharField(max_length=50, verbose_name='responsável')
    logradouro = models.CharField(max_length=50)
    numero = models.IntegerField()
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    uf = models.CharField(max_length=2, verbose_name='UF')
    cep = models.CharField(max_length=50, verbose_name='CEP')
    data_cadastro = models.DateField()
    # contato
    telefone = models.CharField(max_length=50)
    fax = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.nome


class Banco(models.Model):
    nome = models.CharField(max_length=50)
    agencia = models.IntegerField(verbose_name='agência')
    telefone = models.CharField(max_length=50)
    fax = models.CharField(max_length=50)
    contato = models.CharField(max_length=50, verbose_name='pessoa de contato')
    # endereco
    logradouro = models.CharField(max_length=50)
    numero = models.IntegerField()
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    uf = models.CharField(max_length=2, verbose_name='UF')
    cep = models.CharField(max_length=50, verbose_name='CEP')
    data_cadastro = models.DateField()

    def __str__(self):
        return str(self.agencia) + " " + self.nome


class Terceiro(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=50, verbose_name='CPF')
    rg = models.CharField(max_length=50, verbose_name='RG')
    telefone = models.CharField(max_length=50)
    email = models.EmailField()
    logradouro = models.CharField(max_length=50)
    numero = models.IntegerField()
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    uf = models.CharField(max_length=2, verbose_name='UF')
    cep = models.CharField(max_length=50, verbose_name='CEP')
    data_cadastro = models.DateField()
    negativado = models.BooleanField()
    limite_compra = models.FloatField(verbose_name='limite de compra')

    def __str__(self):
        return self.nome


class Cheque(models.Model):
    TIPO_CHEQUE = (
        (1, "Cheque Pré"),
    )
    numero_cheque = models.IntegerField()
    banco = models.ForeignKey(Banco)
    tipo = models.IntegerField(choices=TIPO_CHEQUE)
    data_entrada = models.DateField()
    data_desconto = models.DateField()
    valor = models.FloatField()
    numero_nota = models.IntegerField()
    fornecedor = models.ForeignKey(Fornecedor)
    observacao = models.TextField()
    despesa = models.BooleanField()
    data_cadastro = models.DateField()

    def __str__(self):
        return str(self.numero_cheque) + " " + str(self.fornecedor)
