from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import RequestContext

from .models import Pregunta

# Create your views here.

def index( request, nombre = '' ):

	if( nombre != '' ):
		
		return HttpResponse( "Hola, " + nombre + ". Has llegado al index de las encuestas, con la salida a la vista en bruto." )

	else:

		lista_ultimas_preguntas = Pregunta.objects.order_by('-f_pub')[:5]
		
		# salida = "Hola, cacho de carne. Has llegado al index de las encuestas.<br>"
		# salida += ', '.join([p.pregunta_texto for p in lista_ultimas_preguntas])
		# return HttpResponse( salida )
		
		contexto = {
			'lista_ultimas_preguntas': lista_ultimas_preguntas,
		}

		return render( request, 'encuestas_app/index.html', contexto )
	


def detalle(request, pregunta_id):

	try:
		pregunta = Pregunta.objects.get(pk = pregunta_id)

	except Pregunta.DoesNotExist:

		raise Http404( "La pregunta no existe" )	# Ejemplo con Http404

	# return HttpResponse("Estás viendo la pregunta %s." % pregunta_id)
	return render( request, 'encuestas_app/detalle.html', {'pregunta': pregunta} )


def resultados(request, pregunta_id):

	# response = "Estás viendo los resultados de la pregunta %s."
	# return HttpResponse(response % pregunta_id)
	pregunta = get_object_or_404( Pregunta, pk = pregunta_id )
	return render( request, 'encuestas_app/resultados.html', {'pregunta': pregunta} )



def votar(request, pregunta_id):

	return HttpResponse("Estás votando en la pregunta %s." % pregunta_id)