from django.db import models

# Create your models here.
class Empresa(models.Model):
    nome = models.CharField(max_length=255, verbose_name='Nome')
    area=(
        ('H', 'Saúde'),
        ('T', 'Tecnologia'),
        ('E', 'Construção Civil'),
        ('L', 'Logistica'),
        ('M', 'Metalurgica'),
        ('S', 'Segurança')
    )
    Area_de_Atuação = models.CharField(max_length=100)
    cnpj = models.IntegerField()
    email = models.EmailField(max_length=255, verbose_name='E-mail')
    telefone = models.IntegerField()
    ativo = models.BooleanField(default=True)

def __str__(self):
    return self.nome