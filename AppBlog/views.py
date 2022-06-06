from django.shortcuts import render
from django.http import HttpResponse
from AppBlog.models import Curso
# Create your views here.

def curso(self):
    curso=Curso(nombre="Desarrollo backend", camada=18340)
    curso.save()
    documento = f"Curso: {curso.nombre} - Camada: {curso.camada}"
    return HttpResponse(documento)

def profesores(self):
    documento = f"Pagina de profesores"
    return HttpResponse(documento)

def entregables(self):
    documento = f"Pagina de entregables"
    return HttpResponse(documento)

def estudiantes(self):
    documento = f"Pagina de estudiantes"
    return HttpResponse(documento)
