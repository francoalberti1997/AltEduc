from django.shortcuts import render, HttpResponse
import requests
# Create your views here.

def home(request):
    return render(request, "index.html")

def busqueda(request):
    response = requests.get('http://127.0.0.1:8000/api/home/')
    respuesta = response.json()
    print(respuesta)
    return HttpResponse("ok")