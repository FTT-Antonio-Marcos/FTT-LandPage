from django.shortcuts import render
def home(request):
    return render(request, 'index.html')

def projetos(request):
    return render(request, 'projetos.html')

def integrantes(request):
    return render(request, 'integrantes.html')

def curso(request):
    return render(request, 'curso.html')

def fale_conosco(request):
    return render(request, 'fale_conosco.html')

def solicitacao_projetos(request):
    return render(request, 'solicitacao_projetos.html')

# Create your views here.
