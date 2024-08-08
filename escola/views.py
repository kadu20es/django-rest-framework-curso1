#from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse

def estudantes(request):
    if request.method == 'GET':
        estudante = {
            'id': '1',
            'nome': 'Tiago',
            'idade': '41'
        }
        return JsonResponse(estudante)
