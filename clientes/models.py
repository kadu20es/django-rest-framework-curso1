from django.db import models

# Create your models here.
class Cliente(models.Model):
    GENERO = (
        ('H', 'HOMEM'),
        ('M', 'MULHER'),
        ('A', 'ASSEXUAL'),
        ('I', 'INTERSEX'),
    )
    SEXO = (
        ('F', 'FEMININO'),
        ('M', 'MASCULINO'),
    )
    nome = models.CharField(max_length = 100)
    sobrenome = models.CharField(max_length = 100)
    cpf = models.CharField(max_length = 11)
    data_nascimento = models.DateField()
    genero = models.CharField(max_length = 2, choices = GENERO, blank = False, null = False)
    sexo = models.CharField(max_length = 1, choices = SEXO, blank = False, null = False) 