from django.shortcuts import render

# Create your views here.

def saludo(request):

	return render( request, 'inicio/index.html' )