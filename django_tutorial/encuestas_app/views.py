from django.shortcuts import render, get_object_or_404		# 404: Ejemplo de get_object...
from django.http import HttpResponse, Http404, HttpResponseRedirect		# 404: Ejemplo de Http404
from django.template import RequestContext
from django.urls import reverse		# Redireccion al form de Votar
from django.views import generic	# Factorizacion para un template
from django.utils import timezone	# Actualizacion vista de preguntas - desde tests.py

from .models import Pregunta, Eleccion

# Create your views here.
# Vistas genericas: https://docs.djangoproject.com/es/2.1/ref/class-based-views/generic-display/
	# Cada view genérica necesita saber sobre qué modelo actuar:
	# Atributo model = Pregunta
	# DetailView captura la clave primaria de URL con "pk=pregunta_id"
	# DetailView usa un template llamado <app name>/<model name>_detail.html.
	# Atributo template_name =  "polls/question_detail.html" - Indica a Django que use un template de nombre específico en lugar de usar el nombre de template autogenerado por defecto. 
	# También especificamos template_name para la view results – esto nos asegura que la view de resultados y la de detalle tiene un aspecto diferente al renderizarse, aún cuando ambas usan DetailView por detrás.

	# Los templates recibían un contexto que contenía las variables question y latest_question_list. 
	# Para DetailView la variable question es provista automáticamente – como estamos usando un modelo Django (Question), Django puede determinar un nombre adecuado para la variable de contexto. 
	# Para ListView, el nombre de variable de contexto generado automáticamente es question_list. 
	# Para sobreescribir este valor, pasamos la opción context_object_name, 
	# especificando que queremos usar latest_question_list como nombre. 

class IndexView( generic.ListView ):

	template_name = 'encuestas_app/index.html'
	context_object_name = 'lista_ultimas_preguntas'
	# context_object_name = ('lista_ultimas_preguntas', 'nombre' )

	# def get_query_str(self):	# version 1.8
	def get_queryset(self):		# version 2.1

		# """ Devuelve las 5 ultimas preguntas """
		# return Pregunta.objects.order_by('-f_pub')[:5]

		''' Devuelve las 5 últimas preguntas sin contar las futuras '''
		# Devuelve un queryset de instancias cuyo campo pub_date es menor o igual a timezone.now.
		return Pregunta.objects.filter(
			f_pub__lte = timezone.now()
		).order_by('-f_pub')[:5]


	# List necesita queryset, modelo ... 
	# def get_context_data(self, **kwargs):
		
	# 	return Pregunta.objects.order_by('-f_pub')[:5]
		
	# 	context = super().get_context_data(**kwargs)
	# 	context['now'] = timezone.now()
	# 	return context

class DetalleView( generic.DetailView ):

	model = Pregunta
	template_name = "encuestas_app/detalle.html"

	def get_queryset(self):

		''' Devuelve 404 si la fecha de la pregunta es futura '''
		return Pregunta.objects.filter( f_pub__lte = timezone.now() )


class ResultadosView( generic.DetailView ):

	model = Pregunta
	template_name = "encuestas_app/resultados.html"


# FACTORIZACION A UN TEMPLATE - generic
# def index( request, nombre = 'cacho de carne' ):

# 	# Antiguo - Salida a vista en Bruto
# 	# return HttpResponse( "Hola, " + nombre + ". Has llegado al index de las encuestas, con la salida a la vista en bruto." )

# 	lista_ultimas_preguntas = Pregunta.objects.order_by('-f_pub')[:5]
	
# 	# salida = "Hola, cacho de carne. Has llegado al index de las encuestas.<br>"
# 	# salida += ', '.join([p.pregunta_texto for p in lista_ultimas_preguntas])
# 	# return HttpResponse( salida )
	
# 	contexto = {
# 		'nombre' : nombre,
# 		'lista_ultimas_preguntas': lista_ultimas_preguntas,
# 	}

# 	return render( request, 'encuestas_app/index.html', contexto )
	

# def detalle(request, pregunta_id):

# 	try:
# 		pregunta = Pregunta.objects.get(pk = pregunta_id)

# 	except Pregunta.DoesNotExist:

# 		raise Http404( "La pregunta no existe" )	# 404: Ejemplo con Http404

# 	# return HttpResponse("Estás viendo la pregunta %s." % pregunta_id)
# 	return render( request, 'encuestas_app/detalle.html', {'pregunta': pregunta} )


# def resultados(request, pregunta_id):

# 	# response = "Estás viendo los resultados de la pregunta %s."
# 	# return HttpResponse(response % pregunta_id)
# 	pregunta = get_object_or_404( Pregunta, pk = pregunta_id ) # 404: Ejemplo con get_object_or_404
# 	return render( request, 'encuestas_app/resultados.html', {'pregunta': pregunta} )



def votar(request, pregunta_id):

	# Implementacion basica
	# return HttpResponse("Estás votando en la pregunta %s." % pregunta_id)

	p = get_object_or_404( Pregunta, pk = pregunta_id )

	try:
		opcion_elegida = p.eleccion_set.get( pk = request.POST['eleccion'] )

	except( KeyError, Eleccion.DoesNotExist ):
		# Volver a mostrar el formulario de elecciones
		return render( request, 'encuestas_app/detalle.html', {
			'pregunta': p,
			'mensaje_error': "No has elegido nada"
		})

	else:
		opcion_elegida.votos += 1
		opcion_elegida.save()

		# Siempre devolver un redirect despues de enviardatos con post
		# Asi se evita el reenvio accidental por pulsar dos veces
		return HttpResponseRedirect( reverse('encuestas:resultados', args = (p.id,)) )
