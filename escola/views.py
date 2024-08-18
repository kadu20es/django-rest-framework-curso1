#pylint: disable=C0114, C0115, C0301, E0015, E1101
from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from escola.models import Estudante, Curso, Matricula
from escola.serializers import (
    EstudanteSerializer,
    CursoSerializer,
    MatriculaSerializer,
    ListaMatriculaEstudantesSerializer,
    ListaMatriculasCursoSerializer
)


class EstudanteViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication] # adiciona segurança
    permission_classes = [IsAuthenticated] # adiciona segurança
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer # nome da variável precisa ser esses

class CursoViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication] # adiciona segurança
    permission_classes = [IsAuthenticated] # adiciona segurança
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication] # adiciona segurança
    permission_classes = [IsAuthenticated] # adiciona segurança
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

class ListaMatriculaEstudante(generics.ListAPIView): # lista todas as matrículas de um estudante
    authentication_classes = [BasicAuthentication] # adiciona segurança
    permission_classes = [IsAuthenticated] # adiciona segurança
    def get_queryset(self):
        queryset = Matricula.objects.filter(estudante_id = self.kwargs['pk']) # pega as informações que vem pela URL
        return queryset
    serializer_class = ListaMatriculaEstudantesSerializer

class ListaMatriculaCurso(generics.ListAPIView):
    authentication_classes = [BasicAuthentication] # adiciona segurança
    permission_classes = [IsAuthenticated] # adiciona segurança
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id = self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasCursoSerializer