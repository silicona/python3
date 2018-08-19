import datetime

from django.utils import timezone
from django.test import TestCase, Client
from django.urls import reverse

from .models import Pregunta

# Create your tests here.
# Documentacion: https://docs.djangoproject.com/es/2.1/topics/testing/tools/

# Helper para TestPreguntaVistas
def crear_pregunta( texto, dias ):

	''' Crea una pregunta para test '''

	f_pub = timezone.now() + datetime.timedelta( days = dias )

	return Pregunta.objects.create( pregunta_texto = texto, f_pub = f_pub )


class TestPreguntaModelosMetodos(TestCase):

	@classmethod
	def setUpTestData(clase):

		clase.ahora = timezone.now()


	def test_recien_publicada_con_fecha_reciente(self):

		''' Debería devolver True si la fecha tiene menos de un día '''

		fecha = self.ahora - datetime.timedelta( hours = 1 )
		pregunta_reciente = Pregunta( f_pub = fecha )

		self.assertEqual( pregunta_reciente.recien_publicada(), True )


	def test_recien_publicada_con_fecha_antigua(self):

		''' Debería devolver False con fecha antigua '''

		fecha = self.ahora - datetime.timedelta( days = 30 )
		pregunta_antigua = Pregunta( f_pub = fecha )

		self.assertEqual( pregunta_antigua.recien_publicada(), False )


	def test_recien_publicada_con_fecha_futura(self):

		''' Debería devolver false si la fecha es futura - Correcion en models.py '''

		fecha = self.ahora + datetime.timedelta( days = 30 )
		pregunta_futura = Pregunta( f_pub = fecha )

		self.assertEqual( pregunta_futura.recien_publicada(), False )


class TestPreguntaVistasIndex( TestCase ):

	# response extrae los datos que la view pone en el contexto.
	# response.context_data['lista_ultimas_preguntas'] extrae los datos que la view pone en el contexto.

	@classmethod
	def setUpTestData(clase):

		clase.mensaje_sin = '¡No hay preguntas disponibles, simio babeante!'


	# def setUp(self):

		# self.client = Client()


	def test_vista_index_sin_preguntas(self):

		''' Sin preguntas, debería mostrar un mensaje adecuado '''

		response = self.client.get( reverse('encuestas:index') )

		self.assertEqual( response.status_code, 200 )
		self.assertContains( response, self.mensaje_sin )
		self.assertQuerysetEqual( response.context_data['lista_ultimas_preguntas'], [] )


	def test_vista_index_con_pregunta_antigua(self):

		''' Las preguntas con fecha antigua se deberian mostrar '''

		crear_pregunta( texto = 'Pregunta anterior', dias = -30 )
		response = self.client.get( reverse('encuestas:index') )

		self.assertQuerysetEqual( 
			response.context_data['lista_ultimas_preguntas'],
			['<Pregunta: Pregunta anterior>'] 
		)


	def test_vista_index_con_pregunta_futura(self):

		''' Las preguntas futuras no se publican en index '''

		crear_pregunta( texto = 'Pregunta futura', dias = 20 )
		response = self.client.get( reverse('encuestas:index') )

		self.assertContains( response, self.mensaje_sin, status_code = 200 )
		self.assertQuerysetEqual( response.context_data['lista_ultimas_preguntas'], [] )


	def test_vista_index_con_las_dos_preguntas(self):

		''' Con ambos tipos, solo deberían verse las pasadas '''

		crear_pregunta( texto = 'Pregunta anterior', dias = -30 )
		crear_pregunta( texto = 'Pregunta futura', dias = 30 )

		response = self.client.get( reverse('encuestas:index') )

		self.assertQuerysetEqual(
			response.context_data['lista_ultimas_preguntas'],
			['<Pregunta: Pregunta anterior>']
		)


	def test_vista_index_con_dos_preguntas_pasadas(self):

		''' Con dos preguntas pasadas, se deberían ver las dos '''

		crear_pregunta( texto = 'Pregunta antigua', dias = -28 )
		crear_pregunta( texto = 'Pregunta menos antigua', dias = -20 )

		response = self.client.get( reverse('encuestas:index') )

		self.assertQuerysetEqual(
			response.context_data['lista_ultimas_preguntas'],
			['<Pregunta: Pregunta menos antigua>', '<Pregunta: Pregunta antigua>']
		)


class TestPreguntaVistasDetalle( TestCase ):

	def test_vista_con_pregunta_futura(self):

		pregunta_futura = crear_pregunta( texto = 'Pregunta futura', dias = 30 )

		response = self.client.get( reverse('encuestas:detalle', args = (pregunta_futura.id,)) )

		self.assertEqual( response.status_code, 404 )


	def test_vista_con_pregunta_antigua(self):

		pregunta_antigua = crear_pregunta( texto = 'Pregunta antigua', dias = - 10 )

		response = self.client.get( reverse('encuestas:detalle', args = (pregunta_antigua.id,)) )

		self.assertContains( response, pregunta_antigua.pregunta_texto, status_code = 200 )

		