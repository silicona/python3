from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def saludo(request):

	return render( request, "mi_app/template/saludo.html", {} )

def saludo_bruto( request, numero ):

	texto = "<h1>Bienvenido a Django en Bruto con el número %s " % numero

	return HttpResponse( texto )

