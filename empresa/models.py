from django.db import models

# Create your models here.
class Empresa(models.Model):
    nome = models.CharField(max_length=255, verbose_name='Nome')
    cnpj = models.CharField(max_length=255, verbose_name='CPF')
    email = models.EmailField(max_length=255, verbose_name='E-mail')
    telefone = models.CharField(max_length=255, verbose_name='Telefone')
    ativo = models.BooleanField(default=True)
