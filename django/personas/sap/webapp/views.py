from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def bienvenido(request):
    return HttpResponse('Hola Mundo desde Django')

def despedirse(request):
    return HttpResponse('Despedida desde django')

def contacto(request):
    return HttpResponse('Mi num es: 113231')
    