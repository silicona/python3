import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Pregunta( models.Model ):

	pregunta_texto = models.CharField( max_length = 200 )
	f_pub = models.DateTimeField( 'Fecha de publicación' )

	def __str__(self):	# Python2: __unicode__()

		return self.pregunta_texto


	def recien_publicada(self):

		return self.f_pub >= timezone.now() - datetime.timedelta( days = 1 )

	# Modificaciones en la vista de Admin (encuestas_app/admin.py)
	recien_publicada.admin_order_field = 'f_pub'		
	recien_publicada.boolean = True
	recien_publicada.short_description = 'Recientemente publicada?'


class Eleccion( models.Model ):

	pregunta = models.ForeignKey( Pregunta, on_delete = models.CASCADE )	# Relación 1-1: Cada Eleccion pretenece a una Pregunta
	eleccion_texto = models.CharField( max_length = 200 )
	votos = models.IntegerField( default = 0 )

	def __str__(self):

		return self.eleccion_texto


