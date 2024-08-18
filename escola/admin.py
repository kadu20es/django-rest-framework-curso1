from django.contrib import admin
from escola.models import Estudante, Curso, Matricula

# Register your models here.
class Estudantes(admin.ModelAdmin): # herdando ModelAdmin
    list_display = ('id', 'nome', 'email', 'cpf', 'data_nascimento', 'telefone')
    list_display_links = ('id', 'nome',)
    list_per_page = 20 # resultados por página
    search_fields = tuple('nome',) # permite pesquisar pelo parâmetro informado

# registrar o modelo com o nosso modelo e modelo do admin (acima)
admin.site.register(Estudante, Estudantes)

class Cursos(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'descricao')
    list_display_links = ('id', 'codigo',)
    search_fields = tuple('codigo')

admin.site.register(Curso, Cursos)

class Matriculas(admin.ModelAdmin):
    list_display = ('id', 'estudante', 'curso', 'periodo')
    list_display_links = ('id',)

admin.site.register(Matricula, Matriculas)
