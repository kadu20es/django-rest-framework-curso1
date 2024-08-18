from rest_framework import serializers
from escola.models import Estudante, Curso, Matricula

class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante # modelo utilizado
        fields = ['id', 'nome', 'cpf', 'data_nascimento', 'telefone']
        # filtra os campos desejados

class CursoSerializer(serializers.ModelSerializer):
        class Meta:
            model = Curso
            fields = '__all__'
            # fields = '__all__' traz todos os campos
            # exclude = ['campo'] traz todos os campos, exceto os mencionados aqui

class MatriculaSerializer(serializers.ModelSerializer):
     class Meta:
          model = Matricula
          exclude = [] # não exclui nenhum campo

class ListaMatriculaEstudantesSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source = 'curso.descricao')
    periodo = serializers.SerializerMethodField()
    aluno = serializers.ReadOnlyField(source = 'estudante.nome')
    # captura a informação visível do banco de dados
    class Meta:
         model = Matricula
         fields = ['curso', 'periodo', 'aluno']

    def get_periodo(self, obj):
        return obj.get_periodo_display() # obtém a legenda/descrição que representa o dado a partir do model
    
class ListaMatriculasCursoSerializer(serializers.ModelSerializer):
     id = serializers.ReadOnlyField(source = 'curso.id')
     curso = serializers.ReadOnlyField(source = 'curso.descricao')
     aluno = serializers.ReadOnlyField(source = 'estudante.nome')

     class Meta:
          model = Matricula
          fields = ['id','curso','aluno']