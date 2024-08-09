from rest_framework import serializers
from escola.models import Estudante, Curso

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
