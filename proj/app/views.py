from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, 'index.html')

def comidas(request):
    listaComidas = ['macarrao', 'acaraje', 'fondue', 'sushi']
    
    parametros = {
        'nome': 'comidas:',
        'comidas': listaComidas
    }

    return render(request, 'comidas.html', parametros)
