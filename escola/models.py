from django.db import models

# ID será gerado automaticamente para estudante e curso
class Estudante(models.Model):
    nome = models.CharField(max_length = 100) # campo de caracteres
    email = models.EmailField(blank = False, max_length = 60) # blank = False significa que não pode estar em branco + tamanho de caracteres
    cpf = models.CharField(max_length = 11)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length = 14)

    def __str__(self):
        return self.nome
    
class Curso(models.Model):
    NIVEL = (
        ('B', 'Basico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado'),
    )
    codigo = models.CharField(max_length = 10)
    descricao = models.CharField(blank = False, max_length = 200)
    nivel = models.CharField(max_length = 1, choices = NIVEL, blank = False, null = False, default = 'B')

    def __str__(self):
        return self.codigo
    
class Matricula(models.Model):
    PERIODO = (
        ('M', 'Matutino'),
        ('V', 'Vespertino'),
        ('N', 'Noturno'),
    )
    estudante = models.ForeignKey(Estudante, on_delete = models.CASCADE)
    '''
    #ao deletar o estudante, deleta a matricula associada
    '''
    curso = models.ForeignKey(Curso, on_delete = models.CASCADE)
    periodo = models.CharField(max_length = 1, choices = PERIODO, blank = False, null = False, default = 'M')



