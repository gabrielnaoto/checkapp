from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
from django.utils import timezone


class TemContato(models.Model):
    telefone = models.CharField(max_length=50)
    fax = models.CharField(max_length=50)
    email = models.EmailField()

    class Meta:
        abstract = True

class TemEndereco(models.Model):
    logradouro = models.CharField(max_length=50)
    numero = models.IntegerField()
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    uf = models.CharField(max_length=2, verbose_name='UF')
    cep = models.CharField(max_length=50, verbose_name='CEP')

    class Meta:
        abstract = True


class Empresa(TemEndereco, models.Model):
    nome = models.CharField(max_length=50)
    cnpj = models.CharField(max_length=50, verbose_name='CNPJ')
    ie = models.CharField(max_length=50, verbose_name='inscrição estadual')
    # contato
    telefone = models.CharField(max_length=50)
    fax = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class User(AbstractUser):
    empresa = models.ForeignKey(Empresa, null=True, blank=True)



class Fornecedor(TemContato, TemEndereco, models.Model):
    TIPO_PESSOA = (
        (1, 'PESSOA FÍSICA'),
        (2, 'PESSOA JURÍDICA'),
    )
    nome = models.CharField(max_length=50)
    tipo = models.IntegerField(choices=TIPO_PESSOA, verbose_name='Tipo de pessoa')
    cpf_cnpj = models.CharField(max_length=50, verbose_name='CPF/CNPJ')
    ie = models.CharField(max_length=50, verbose_name='inscrição estadual', blank=True, null=True)
    rg = models.CharField(max_length=50, verbose_name='RG', blank=True, null=True)
    responsavel = models.CharField(max_length=50, verbose_name='responsável')
    data_cadastro = models.DateField(default=timezone.now)


    def __str__(self):
        return self.nome


class Banco(TemContato, TemEndereco, models.Model):
    nome = models.CharField(max_length=50)
    agencia = models.IntegerField(verbose_name='agência')
    contato = models.CharField(max_length=50, verbose_name='pessoa de contato')
    data_cadastro = models.DateField(default=timezone.now)

    def __str__(self):
        return str(self.agencia) + " " + self.nome


class Cliente(TemContato, TemEndereco, models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=50, verbose_name='CPF')
    rg = models.CharField(max_length=50, verbose_name='RG')
    data_cadastro = models.DateField(default=timezone.now)

    def __str__(self):
        return self.nome


class Cheque(models.Model):
    TIPO_CHEQUE = (
        (1, "Cheque Pré"),
        (2, "Cheque Pós"),
    )
    numero_cheque = models.IntegerField()
    banco = models.ForeignKey(Banco)
    tipo = models.IntegerField(choices=TIPO_CHEQUE)
    # data_entrada = models.DateField()
    data_desconto = models.DateField()
    valor = models.FloatField()
    data_cadastro = models.DateField(default=timezone.now)

    class Meta:
        abstract = True

class Recebido(Cheque):
    # data_lancamento = models.DateField()
    cliente = models.ForeignKey(Cliente)
    tem_fundo = models.BooleanField(default=True)
    foi_repassado = models.BooleanField(default=False)
    foi_compensado = models.BooleanField(default=False)
    repassado = models.ForeignKey(Fornecedor, blank=True, null=True)

    def __str__(self):
        return str(self.numero_cheque)

class Emitido(Cheque):
    numero_nota = models.IntegerField()
    fornecedor = models.ForeignKey(Fornecedor)
    observacao = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.numero_cheque)

